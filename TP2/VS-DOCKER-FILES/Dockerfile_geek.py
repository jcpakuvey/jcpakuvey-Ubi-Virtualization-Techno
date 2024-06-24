FROM ubuntu:latest

# Instalar dependências
RUN apt-get update && apt-get install -y \
    wget \
    python3 \
    python3-pip \
    unzip

# Baixar e instalar o Geekbench
RUN wget https://cdn.geekbench.com/Geekbench-5.4.1-Linux.tar.gz && \
    tar -xzvf Geekbench-5.4.1-Linux.tar.gz && \
    mv Geekbench-5.4.1-Linux /opt/geekbench

# Copiar o aplicativo Python para o contêiner
COPY app2.py /app/app2.py
WORKDIR /app

# Comando padrão para rodar o Geekbench
CMD ["/opt/geekbench/geekbench5"]