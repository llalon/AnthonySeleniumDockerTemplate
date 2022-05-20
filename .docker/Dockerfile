FROM ubuntu:20.04 AS build

WORKDIR /build
COPY . .

RUN echo "**** install build dependencies ****" && \
    apt-get update && \
    apt-get install -y python3-pip python-is-python3 python3-venv

RUN	echo "**** building python package ****" && \
    pip install --upgrade pip && \
    python setup.py sdist

FROM selenium/standalone-chrome AS run

WORKDIR /app
ENV PATH=$HOME/.local/bin:$PATH
COPY --from=0 /build/dist/* ./

RUN echo "**** install dependencies ****" && \
    sudo apt-get update && \
    sudo apt-get install -y python3-pip python-is-python3

RUN echo "**** install package ****" && \
    pip install --upgrade pip && \
    pip install wheel setuptools \
    pip install *.tar.gz

RUN	echo "**** cleanup ****" && \
    sudo apt-get clean && \
    sudo rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/* \
    /app/*

# make cli default command
CMD anthony --help