FROM python:3.7-alpine
ENV PYTHONUNBUFFERED=0
RUN mkdir /repo
WORKDIR /repo
COPY requirements.txt /repo/requirements.txt
RUN pip install -r /repo/requirements.txt
COPY . /repo