FROM python:3.7-alpine
RUN apk update && \
    apk add --virtual build-deps gcc musl-dev && \
    apk add postgresql-dev
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY app.py /src
COPY temp.png /src
COPY bookapi /src/bookapi
COPY database /src/database
CMD python /src/app.py
