FROM python:3.9-slim-buster

WORKDIR /home/app/web

COPY compose/production/django/entrypoint.sh induction_back-app/requirements/base.txt induction_back-app/requirements/production.txt /

RUN    mkdir /home/app/static \
    && mkdir /home/app/media \
    && mkdir /home/app/import_files \
    && mkdir /home/app/logs \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \ 
    && pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r /production.txt \
    && rm /base.txt \
    && rm /production.txt 

COPY ./induction_back-app/manage.py /home/app/web/
COPY ./induction_back-app/apps /home/app/web/apps
COPY ./induction_back-app/src /home/app/web/src

CMD ["/entrypoint.sh"]