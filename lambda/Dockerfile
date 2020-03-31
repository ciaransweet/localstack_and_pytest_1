FROM python:3.6

RUN apt update && apt install -y netcat && apt clean

WORKDIR /lambda

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ./runtests.sh
