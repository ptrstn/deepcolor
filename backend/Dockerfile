FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY testing-requirements.txt /code/
RUN python -m venv venv
RUN pip install -r testing-requirements.txt
COPY . /code/
RUN pip install -e /code
RUN python manage.py migrate