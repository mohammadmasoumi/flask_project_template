FROM python:3.9

LABEL MAINTAINER="Mohammad Masoumi mohammad.masoomy74@gmail.com"

ENV GROUP_ID=2000 \
    USER_ID=2000 \
    USER_NAME=flask



COPY /app /src/app
WORKDIR src

RUN apt-get update \
    && apt-get -y install libsnappy-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install pip --upgrade pip \
    && pip install -r requirements/production.txt \
    && addgroup -gid $GROUP_ID $USER_NAME  \
    && useradd -u $USER_ID -g $USER_NAME -ms /bin/bash $USER_NAME

USER $USER_NAME
EXPOSE 5000