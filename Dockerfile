######################## BASE IMAGE #######################

FROM python:3.11-slim AS base

EXPOSE 80

RUN groupadd --gid 1000 python && \
    useradd --uid 1000 --gid python --shell /bin/bash --create-home python

USER python

WORKDIR /home/python/app

ENV PATH=/home/python/.local/bin:$PATH
ENV PYTHONPATH=/home/python/.local/lib/python3.11/site-packages:$PYTHONPATH

################## BASE IMAGE W/ APT PKGS #################

FROM base AS base-with-apt-packages

USER root

RUN apt-get clean \
    && apt-get -y update \
    && apt-get -y install \
    build-essential \
    python3-dev=3.11.* \
    && rm -rf /var/lib/apt/lists/*

USER python

###################### BASE-DEV IMAGE #####################

FROM base-with-apt-packages AS base-development

COPY --chown=python:python requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

###################### BASE-PROD IMAGE ####################

FROM base-with-apt-packages AS base-production

COPY --chown=python:python deployment/prod.requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install uwsgi==2.0.23 --src /usr/local/src

####################### DEV IMAGE ########################

FROM base AS development

COPY --from=base-development /home/python/.local /home/python/.local

# source code is not copied because it is supposed to be
# bind mounted as a volume.

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "80", "--debug" ]

####################### TEST IMAGE ########################

FROM development AS test

ENV ENVIRONMENT=test

COPY config.py main.py ./
COPY app app
COPY tests tests

CMD [ "python", "-m", "pytest" ]

####################### PROD IMAGE #######################

FROM base AS production

ENV ENVIRONMENT=production

USER root

RUN apt-get clean \
    && apt-get -y update \
    && apt-get -y install nginx=1.22.* sudo \
    && rm -rf /var/lib/apt/lists/* \
    && echo "python ALL=(ALL) NOPASSWD: /usr/sbin/service nginx start" \
    >> /etc/sudoers

USER python

COPY --from=base-production /home/python/.local /home/python/.local
COPY --chown=python:python config.py main.py ./
COPY --chown=python:python deployment deployment
COPY --chown=python:python app app

USER root

RUN mv ./deployment/nginx.conf /etc/nginx/ \
    && chmod +x ./deployment/start.sh

USER python

CMD [ "./deployment/start.sh" ]