import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

#==========================================
#Boas metodologias usadas
#-Usando caras como o Copy() eu armazeno o csv em questao em memoria, assim nao preciso atualizar na mao pra testes (Possivelmente vou criar cenarios onde consigo fazer essa atualizacao dinamica(automatica))
#-Usando o X_Test da pra eu pegar a parecela de clientes pouco percebida, algo que o modelo talvez n vesse
#-Com o delivery_delay_days que é uma das variaveis principais da pra passar algo mais definido como zerar as entregas para testes, ou diminuir o tempo de entrega pela metade
#-Outros comentarios se quiser colocar
#==========================================

# 1. Carregar e preparar os dados, no caso o que foi passado pra teste do teech chalenge
df = pd.read_csv('../../data/raw/desafio_nps_fase_1.csv')

def categorize_nps(score):
    if score <= 6: return 'Detrator'
    elif score <= 8: return 'Neutro'
    else: return 'Promotor'

df['nps_class'] = df['nps_score'].apply(categorize_nps)

# Preparar o x e y das coluns
X = df.drop(columns=['customer_id', 'order_id', 'nps_score', 'nps_class'])
y = df['nps_class']
X = pd.get_dummies(X, columns=['customer_region'], drop_first=True)
X = X.fillna(X.median())

# Aqui eu treino o modelo base
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
model = RandomForestClassifier(random_state=42, n_estimators=100)
model.fit(X_train, y_train)

#Comeco os testes de cenarios, primeiro vou com a base da realidade
print("--- INICIANDO O SIMULADOR DE CENÁRIOS ---\n")
# ==========================================
# CENÁRIO 1: A REALIDADE (Baseline)
# Como a base de teste (20% dos clientes) se comporta hoje
# ==========================================
previsoes_reais = model.predict(X_test)
resultado_real = pd.Series(previsoes_reais).value_counts(normalize=True) * 100
print("1. CENÁRIO ATUAL (Realidade):")
print(resultado_real.round(1).to_string() + " %")


#Vou pro segundo cenario que seria onde tudo é perfeito, algo que pouco acontece..
# ==========================================
# CENÁRIO 2: OTIMISTA (Logística Perfeita)
# Simulando que a empresa zerou os atrasos e entregou tudo rápido
# ==========================================
X_otimista = X_test.copy()
X_otimista['delivery_delay_days'] = 0  # Zerando os atrasos de todo mundo
# Reduzir o tempo de entrega pela metade tambem /2
X_otimista['delivery_time_days'] = X_otimista['delivery_time_days'] // 2

previsoes_otimista = model.predict(X_otimista)
resultado_otimista = pd.Series(previsoes_otimista).value_counts(normalize=True) * 100
print("\n2. CENÁRIO OTIMISTA (Zero Atrasos):")
print(resultado_otimista.round(1).to_string() + " %")


#Mato o ultimo com um cenario caotico, crise de chamados e muitas entregas atrasadas, como a black friday
# ==========================================
# CENÁRIO 3: CAÓTICO (Crise no SAC e Entregas)
# Simulando uma Black Friday que deu muito errado
# ==========================================
X_caotico = X_test.copy()
X_caotico['delivery_delay_days'] = X_caotico['delivery_delay_days'] + 5  # Todo mundo atrasou +5 dias
X_caotico['customer_service_contacts'] = X_caotico['customer_service_contacts'] + 3 # Todo mundo ligou 3 vezes pra reclamar

previsoes_caotico = model.predict(X_caotico)
resultado_caotico = pd.Series(previsoes_caotico).value_counts(normalize=True) * 100
print("\n3. CENÁRIO CAÓTICO (Black Friday Ruim):")
print(resultado_caotico.round(1).to_string() + " %")


# ==========================================
# Gerando graficos pra empresa se necessario, talvez eu nem use isso sinceramente.
# ==========================================
resultados = pd.DataFrame({
    'Atual': resultado_real,
    'Otimista (Sem Atraso)': resultado_otimista,
    'Caótico (Crise)': resultado_caotico
}).fillna(0).T

resultados = resultados[['Detrator', 'Neutro', 'Promotor']] # Ordenar as colunas

resultados.plot(kind='bar', stacked=True, figsize=(10, 6), color=['#e74c3c', '#f1c40f', '#2ecc71'])
plt.title('Simulação de Cenários: Impacto das Operações no NPS', fontsize=14)
plt.ylabel('Porcentagem de Clientes (%)', fontsize=12)
plt.xticks(rotation=0)
plt.legend(title='Classificação', loc='upper right')
plt.show()