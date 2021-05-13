FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir src/
WORKDIR /src

COPY requirements.txt /src/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /src/