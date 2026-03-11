import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

#Carregar os dados do csv passadooo
df = pd.read_csv('../data/raw/desafio_nps_fase_1.csv')

# 2. Defini as variaveis, o seu (target)
# Funcao de categorizar o promotor, neutro e dtrator
def categorize_nps(score):
    if score <= 6:
        return 'Detrator'
    elif score <= 8:
        return 'Neutro'
    else:
        return 'Promotor'

# Criamos uma nova coluna que sera nossa variavel alvo
df['nps_class'] = df['nps_score'].apply(categorize_nps)

# A SELEÇÃO E PREPARAÇÃO DAS VARIÁVEIS DE ENTRADA
# Removi as colunas que não agregam ao modelo (IDs..) e a nota de NPS original(talvez voltamos para notas de nps original, a analisar..)
# (pois não podemos prever a resposta usando ela mesma)
X = df.drop(columns=['customer_id', 'order_id', 'nps_score', 'nps_class'])
y = df['nps_class']

# Transformamos variáveis de texto
X = pd.get_dummies(X, columns=['customer_region'], drop_first=True)

# Preenchemos eventuais valores em branco com a mediana para não dar erro no modelo, dados em brancos podem quebrar
X = X.fillna(X.median())

#  A LÓGICA DE SEPARAÇÃO DOS DADOS
# Dividimos os dados: 80% para o modelo aprender (treino) e 20% para validar (teste).
# O parâmetro 'stratify=y' garante que a mesma proporção de detratores/promotores seja mantida no teste.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# A ESCOLHA DO MODELO
# Optamos pelo Random Forest por ser excelente lidando com muitas variáveis operacionais juntas ---Menos Overfitting
model = RandomForestClassifier(random_state=42, n_estimators=100)
model.fit(X_train, y_train) # Treinando o modelo

# A FORMA DE AVALIAÇÃO DOS RESULTADOS
# usa o predict para adivinhar as classes de grupo de teste
y_pred = model.predict(X_test)

# Retorno de  desempenho real comparando a previsão com o gabarito de analise
print("Relatório de Classificação (Performance do Modelo):")
print(classification_report(y_test, y_pred))