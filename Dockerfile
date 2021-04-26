FROM ubuntu:16.04

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
	apt-get install wget -y && \
	apt-get install python3-pip -y && \
	apt-get install unixodbc unixodbc-dev

WORKDIR /var/www
ADD requirements.txt .
RUN pip3 install -r requirements.txt && \
	apt-get clean 