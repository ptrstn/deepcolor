FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY backend/ backend/
COPY deepcolor/ deepcolor/

RUN pip install -e deepcolor/
RUN pip install -e backend/
RUN python backend/manage.py migrate