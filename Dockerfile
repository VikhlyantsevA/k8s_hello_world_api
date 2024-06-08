FROM --platform=linux/amd64 python:slim

WORKDIR /app

COPY k8s_hello_world.py requirements.txt .

RUN pip3 install -r ./requirements.txt
RUN apt update && apt upgrade
RUN apt install -y curl
RUN apt-get install -y iputils-ping

EXPOSE 5000

CMD ["python3", "./k8s_hello_world.py"]