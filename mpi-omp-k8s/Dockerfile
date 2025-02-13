FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    locales \
    tzdata && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    mpich \
    openmpi-bin \
    libopenmpi-dev \
    gcc \
    g++ \
    make && \
    rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8

COPY . /app
WORKDIR /app

RUN mpicc -o space_exploration space_exploration.c -fopenmp

ENV OMPI_ALLOW_RUN_AS_ROOT=1
ENV OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1

CMD mpirun -np 3 ./space_exploration && tail -f /dev/null
