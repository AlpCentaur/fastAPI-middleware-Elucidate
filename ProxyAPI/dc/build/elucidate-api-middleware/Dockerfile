# base api on latest debian, as it is the securest system for network related tasks

FROM debian:latest


# add user to later work with and get some more security

RUN useradd -ms /bin/bash user


# install dependencies

RUN apt-get update && apt-get install -y pip python

RUN pip install uvicorn fastapi python-multipart passlib[bcrypt] python-jose[cryptography]


CMD cd /opt && uvicorn --host 0.0.0.0 main:app
