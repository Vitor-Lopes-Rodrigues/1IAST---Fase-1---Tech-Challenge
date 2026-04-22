# 📊 Tech Challenge Fase 1 - Case NPS Preditivo

![Fiap Logo](.github/imgs/fiap_header.png)

Bem-vindo ao repositório do projeto de previsão de Net Promoter Score (NPS) para E-commerce, desenvolvido como parte do Tech Challenge da pós-graduação em Data Science e Inteligência Artificial.

## 👥 Membros

* **Gabriela de Lima Lopes** (RM372467) ➔ [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabrieladelimalopes/)
* **Pedro Henrique Gomes** (RM372427) ➔ [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pedrogomes95/)
* **Vitor Lopes Rodrigues** (RM372427) ➔ [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vitor-lopes-rodrigues/)
* **Lucas Oliveira dos Santos Lima** (RM372651) ➔ [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lucasoslima/)
* **Mateus Quintino Vieira dos Santos** (RM371795) ➔ [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mateusqsantos/)

## 🎯 Objetivo do Projeto

O crescimento acelerado do e-commerce trouxe desafios relevantes na experiência do cliente. Atualmente, a satisfação (NPS) é medida apenas de forma **reativa**, após o fim da jornada de compra.

O objetivo deste projeto é transformar dados operacionais (logística, pedidos e atendimento) em insights acionáveis e criar um **Modelo Preditivo** capaz de antecipar a insatisfação do cliente. Isso permite que a empresa atue de forma **proativa** para reverter experiências ruins antes mesmo de a pesquisa de NPS ser enviada.

## 📁 Estrutura do Repositório

O projeto foi estruturado seguindo boas práticas de Ciência de Dados e Engenharia de Software:

```text
├── data/
│   └── raw/                   # Base de dados original em formato CSV
├── docs/
│   └── TECH_Challenge.pdf    # Respostas às questões do Tech Challenge
├── models/
│   └── modelo_nps.pkl         # Modelo preditivo treinado e serializado
├── notebooks/                 # Notebooks com a esteira de análise e modelagem
│   ├── 01_exploracao_de_dados.ipynb    # Análise Exploratória (EDA) e Storytelling
│   ├── 02_modelo_preditivo.ipynb       # Treinamento do classificador Random Forest
│   └── scriptsAutomation/
│       └── 03_simulador_de_cenarios.ipynb  # Teste de stress operacional com dados fictícios
├── .gitignore                 # Arquivos ignorados pelo versionamento
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação principal
```

## 👨‍💻 Este projeto foi desenvolvido com as seguintes tecnologias

### Python

Linguagem de programação principal do projeto, utilizada para análise de dados, treinamento do modelo preditivo e automação dos pipelines de processamento.

### Jupyter Notebook

Ambiente interativo para desenvolvimento e documentação das análises exploratórias, modelagem e simulações, combinando código, visualizações e narrativa em um único documento.

### Pandas

Biblioteca para manipulação e análise de dados tabulares, utilizada no carregamento, limpeza, transformação e agregação do dataset de NPS.

### Scikit-learn

Biblioteca de Machine Learning utilizada para treinar o modelo preditivo de classificação do NPS (Random Forest), além de realizar pré-processamento, avaliação e exportação do modelo.

### Matplotlib & Seaborn

Bibliotecas de visualização de dados utilizadas para gerar os gráficos exploratórios e de storytelling ao longo da análise.

### NumPy

Biblioteca de computação numérica utilizada como suporte às operações matemáticas e manipulação de arrays durante a modelagem.

---

### Pré-requisitos

Para executar este projeto, é necessário ter instalado:

- `Python 3.8+`

---

## 🚀 Instalação e Execução

### Instalação

Para instalar e configurar o projeto, siga os passos abaixo:

1 Clone o repositório:

```bash
git clone git@github.com:Vitor-Lopes-Rodrigues/1IAST---Fase-1---Tech-Challenge.git
```

2 Navegue até o diretório do projeto:

```bash
cd 1IAST---Fase-1---Tech-Challenge
```

3 Instale as dependências:

```bash
pip install -r requirements.txt
```

### Executando o projeto

1. Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

2. Abra os notebooks na seguinte ordem recomendada:

- `notebooks/01_exploracao_de_dados.ipynb` — Análise Exploratória (EDA) e Storytelling
- `notebooks/02_modelo_preditivo.ipynb` — Treinamento do modelo preditivo
- `notebooks/scriptsAutomation/03_simulador_de_cenarios.ipynb` — Simulador de cenários operacionais

---

## 🐳 Executando a API com Docker

### Execução

1. Build o arquivo docker:

```bash
- docker build -t api-nps .
```

2. Após o término da construção, inicie o container mapeando para a porta 8000:

```bash
docker run -d -p 8000:8000 api-nps
```

3. Após o Build corretamente, navegar até

```bash
http://localhost:8000/docs#/
```

4. Esta api funciona apenas para o modelo preditivo de NPS, favor seguir documentações do localhost 

---

### Apresentação do trabalho

Link para o video: [Post Tech Fiap Fase01](https://youtu.be/lT-LJhv4dkk?si=34HSy8P3PjABmCnu)
