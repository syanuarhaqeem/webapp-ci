# base image
FROM python:3.12-slim

RUN useradd -m webappu --no-log-init
USER webappu
WORKDIR /home/webappu

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY app.py .
COPY healthcheck.py .
COPY database.py .

EXPOSE 3000

CMD ["python3", "app.py"]
