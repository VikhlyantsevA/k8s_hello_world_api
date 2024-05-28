FROM python:slim

WORKDIR /app

COPY k8s_hello_world.py requirements.txt .

RUN pip3 install -r ./requirements.txt

EXPOSE 5001:5000

CMD ["python3", "./k8s_hello_world.py"]