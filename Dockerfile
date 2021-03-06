FROM python:3.10-slim AS bot

# Env vars
ENV TG_TOKEN ${TG_TOKEN}

RUN apt-get update
RUN apt-get install -y python3 python3-pip python-dev build-essential python3-venv

RUN mkdir -p /codebase /storage
ADD . /codebase
WORKDIR /codebase

RUN pip3 install -r requirements.txt
RUN chmod +x /codebase/main.py

CMD python3 /codebase/main.py