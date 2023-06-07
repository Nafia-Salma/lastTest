FROM python:3.8.16-slim-buster AS BASE

RUN apt-get update \
      && apt-get --assume-yes --no-install-recommends install \
      build-essential \
      curl \
      git \
      jq \
      libgomp1 \
      vim 

WORKDIR /app

# Upgrade pip version
RUN pip install --no-cache-dir --upgrade pip

# Install Rasa version 3.5.10
RUN pip install --no-cache-dir rasa pandas

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml
