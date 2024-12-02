FROM python:latest

ADD server.py /server/
ADD requirements.txt /server/
COPY /templates /server/templates
COPY /static /server/static
RUN pip3 install -r server/requirements.txt
COPY /templates /server/templates

WORKDIR /server/