# Image Col Backend 

This is the backend for the image colorizer application.

It consists of 2 packages:
- ```backendsite```: The Django project
- ```imaginator```: The actual app that does all the work

## Setup

Getting started:

```bash
git clone https://github.com/INF-HS-KL-BEGGEL/DL-SS20-T1-image-col
cd DL-SS20-T1-image-col
python -m venv venv
. venv/bin/activate
pip install -e backend/
pip install -r testing-requirements.txt
```

## Run

To run the backend website locally, execute following commands:

```bash
python backend/manage.py migrate
python backend/manage.py runserver
```

Then open [127.0.0.1:8000](127.0.0.1:8000) in your webbrowser

## Entry Points

### Upload image

```
POST /api/v1/images/
```

with:
```
file: <file> 
```

### List images

```
GET /api/v1/images/
```

### List image

```
GET /api/v1/images/<id>/
```

### Delete image

```
DELETE /api/v1/images/<id>/
```

