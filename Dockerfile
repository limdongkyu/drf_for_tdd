FROM python:3.7-alpine
ENV PYTHONUNBUFFERED=0
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app