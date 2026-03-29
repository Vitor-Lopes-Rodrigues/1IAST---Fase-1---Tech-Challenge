# 📊 Tech Challenge Fase 1 - Case NPS Preditivo

Bem-vindo ao repositório do projeto de previsão de Net Promoter Score (NPS) para E-commerce, desenvolvido como parte do Tech Challenge da pós-graduação em Data Science e Inteligência Artificial.

## 🎯 Objetivo do Projeto
O crescimento acelerado do e-commerce trouxe desafios relevantes na experiência do cliente. Atualmente, a satisfação (NPS) é medida apenas de forma **reativa**, após o fim da jornada de compra. 

O objetivo deste projeto é transformar dados operacionais (logística, pedidos e atendimento) em insights acionáveis e criar um **Modelo Preditivo** capaz de antecipar a insatisfação do cliente. Isso permite que a empresa atue de forma **proativa** para reverter experiências ruins antes mesmo de a pesquisa de NPS ser enviada.

## 📁 Estrutura do Repositório
O projeto foi estruturado seguindo boas práticas de Ciência de Dados e Engenharia de Software:

```text
├── data/
│   └── raw/                   # Base de dados original em formato CSV
├── notebooks/                 # Notebooks com a esteira de análise e modelagem
│   ├── 01_exploracao_de_dados.ipynb    # Análise Exploratória (EDA) e Storytelling
│   ├── 02_modelo_preditivo.ipynb       # Treinamento do classificador Random Forest
│   └── 03_simulador_de_cenarios.ipynb  # Teste de stress operacional com dados fictícios
├── .gitignore                 # Arquivos ignorados pelo versionamento
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação principal
