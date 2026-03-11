import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração visual dos gráficos
sns.set_theme(style="whitegrid")

# 1. Carregar os dados
df = pd.read_csv('../data/raw/desafio_nps_fase_1.csv')

# Recriar a categoria de NPS para facilitar a visualização
def categorize_nps(score):
    if score <= 6: return 'Detrator'
    elif score <= 8: return 'Neutro'
    else: return 'Promotor'

df['nps_class'] = df['nps_score'].apply(categorize_nps)

# --- GRÁFICO 1: O Impacto do Atraso na Entrega ---
plt.figure(figsize=(10, 6))
sns.boxplot(x='nps_class', y='delivery_delay_days', data=df, order=['Detrator', 'Neutro', 'Promotor'], palette='Set2')
plt.title('Relação entre Atraso na Entrega e Classe NPS', fontsize=14)
plt.xlabel('Classificação NPS', fontsize=12)
plt.ylabel('Dias de Atraso na Entrega', fontsize=12)
plt.show()

# --- GRÁFICO 2: O Impacto do Atendimento ao Cliente ---
plt.figure(figsize=(10, 6))
sns.barplot(x='nps_class', y='customer_service_contacts', data=df, order=['Detrator', 'Neutro', 'Promotor'], palette='Set1')
plt.title('Média de Contatos com o Atendimento por Classe NPS', fontsize=14)
plt.xlabel('Classificação NPS', fontsize=12)
plt.ylabel('Média de Contatos no Atendimento', fontsize=12)
plt.show()

# --- GRÁFICO 3: Correlação Geral (O que mais afeta a nota?) ---
# Vamos olhar como as variáveis numéricas se correlacionam com a nota original do NPS
colunas_numericas = ['nps_score', 'delivery_delay_days', 'customer_service_contacts', 'delivery_time_days', 'freight_value']
correlacao = df[colunas_numericas].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlacao[['nps_score']].sort_values(by='nps_score', ascending=False),
            annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlação das Variáveis com a Nota de NPS', fontsize=14)
plt.show()