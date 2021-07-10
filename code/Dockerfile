FROM python:3.8

RUN mkdir /code
WORKDIR /code

COPY requirements.txt requirements.txt

RUN apt-get update &&\
    #open-cv issue https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo
    apt-get install -y python3-opencv &&\
    pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    rm requirements.txt

USER developer

COPY . .

CMD ["python", "ocr.py"]