FROM ubuntu:latest

RUN apt-get update && apt-get install -y sysbench python3

COPY . /app
WORKDIR /app

CMD ["sh", "-c", "python3 app2.py & sysbench --test=memory run"]