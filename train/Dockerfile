FROM nvcr.io/nvidia/pytorch:19.09-py3

WORKDIR /colornet

COPY ./pt1/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./pt1  ./
CMD ["python", "train.py"]
