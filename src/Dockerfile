FROM gcr.io/deeplearning-platform-release/r-cpu.4-1:latest

WORKDIR /root

COPY print.r /root/print.r

RUN apt-get update
RUN apt-get install gfortran -yy