FROM python:slim

MAINTAINER LightQuantum

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./jcss ./jcss

CMD ["uvicorn", "jcss:app", "--host", "0.0.0.0", "--limit-concurrency", "32"]