# Usa uma imagem oficial do Python, versão leve
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para dentro do container
COPY requirements.txt .

# Instala as bibliotecas sem guardar cache (deixa a imagem mais leve)
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o restante do código para dentro da pasta /app no container
COPY . .

# Expõe a porta que o FastAPI vai usar
EXPOSE 8000

# Comando para iniciar o servidor da API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]