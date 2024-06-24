FROM ubuntu:latest

RUN apt-get update && apt-get install -y sysbench

CMD ["sysbench", "--test=memory", "run"]