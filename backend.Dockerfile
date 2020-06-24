FROM ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y caffe-cpu
RUN apt-get install -y python-is-python3
RUN apt-get install -y python3-pip
RUN apt-get install -y libgtk2.0-dev

WORKDIR /usr/src/app

ENV GLOG_minloglevel=2
ENV PYTHONUNBUFFERED 1

COPY pytest.ini pytest.ini
COPY backend/ backend/
COPY deepcolor/ deepcolor/

RUN python -m pip install --upgrade pip
RUN python -m pip install  -e deepcolor/
RUN python -m pip install  -e backend/
RUN python backend/manage.py migrate
