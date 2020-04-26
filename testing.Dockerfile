FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY pytest.ini pytest.ini
COPY testing-requirements.txt testing-requirements.txt
COPY backend/ backend/
COPY deepcolor/ deepcolor/

RUN pip install -r testing-requirements.txt
RUN pip install -e deepcolor/
RUN pip install -e backend/
RUN pytest --cov .