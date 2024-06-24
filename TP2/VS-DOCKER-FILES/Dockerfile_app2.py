FROM ubuntu:latest

# Instalar dependências
RUN apt-get update && apt-get install -y \
    wget \
    python3 \
    python3-pip \
    unzip

# Copiar o aplicativo Python para o contêiner
COPY app2.py /app/app2.py
WORKDIR /app

# Comando para rodar o benchmark do aplicativo Python
CMD ["python3", "app2.py"]