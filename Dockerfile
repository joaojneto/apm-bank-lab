# Use a imagem oficial do Python como base
FROM python:3.7-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências, incluindo supervisor
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install supervisor

# Copia o código atual para o diretório de trabalho
COPY . .

# Copia o arquivo de configuração do supervisord
COPY supervisord.conf /etc/supervisord.conf

# Comando para iniciar o supervisord
CMD ["supervisord", "-c", "/etc/supervisord.conf"]
