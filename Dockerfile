# Three RUN commands for better layer reusage. Package installations can be
# cached if no package dependencies are added, and pip installations too as
# long as requirements.txt remains unchanged.

# Reminder: If any new packages are installed in the first RUN with apt-get,
# they must be removed in the second one.

####################### BASE IMAGE #######################

FROM python:3.11-slim AS base

WORKDIR /srv/reef-api

RUN apt-get clean \
    && apt-get -y update \
    && apt-get -y install \
    build-essential \
    nginx=1.22.* \
    python3-dev=3.11.* \
    && rm -rf /var/lib/apt/lists/*

####################### DEV IMAGE ########################

FROM base AS development

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --src /usr/local/src \
    && apt-get -y remove \
    build-essential \
    python3-dev

# source code is not copied because it is supposed to be
# bind mounted as a volume.

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "80", "--debug" ]

####################### TEST IMAGE ########################

FROM development AS test

COPY config.py main.py ./
COPY app app
COPY tests tests

CMD [ "python", "-m", "pytest" ]

####################### PROD IMAGE #######################

FROM base AS production

EXPOSE 80

COPY deployment/prod.requirements.txt requirements.txt

RUN pip install -r requirements.txt --src /usr/local/src \
    && pip install uwsgi==2.0.23 --src /usr/local/src \
    && apt-get -y remove \
    build-essential \
    python3-dev

COPY config.py main.py ./
COPY deployment deployment
COPY app app

RUN mv ./deployment/nginx.conf /etc/nginx/ \
    && chmod +x ./deployment/start.sh

CMD [ "./deployment/start.sh" ]