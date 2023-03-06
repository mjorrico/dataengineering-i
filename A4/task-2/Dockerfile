FROM ubuntu:22.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt install -y openjdk-11-jdk-headless scala wget screen python3 python3-pip
RUN pip3 install pyspark==3.3.2
RUN wget https://archive.apache.org/dist/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz
RUN tar -xvf spark-3.3.2-bin-hadoop3.tgz
RUN rm -rf spark-3.3.2-bin-hadoop3.tgz
RUN mv spark-3.3.2-bin-hadoop3/ /usr/local/spark