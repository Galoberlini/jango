FROM python:3.9-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /home/app/web

COPY induction_back-app/requirements/base.txt induction_back-app/requirements/local.txt /

RUN    mkdir /home/app/static \
    && mkdir /home/app/media \
    && mkdir /home/app/import_files \
    && mkdir /home/app/logs \
    && pip install -U pip \
    && pip install -r /local.txt \
    && rm /base.txt \
    && rm /local.txt 

ADD ./induction_back-app /home/app/web

CMD ["bash"]