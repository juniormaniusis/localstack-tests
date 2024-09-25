# Utiliza uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências
# COPY ../requirements.txt .

# Instala as dependências
RUN pip install boto3 pymysql cryptography --no-cache-dir
# Copia o código da aplicação
COPY . .

# Comando para rodar o script Python
CMD ["python", "main.py"]