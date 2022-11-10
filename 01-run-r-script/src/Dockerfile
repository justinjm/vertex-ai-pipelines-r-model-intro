
FROM gcr.io/deeplearning-platform-release/r-cpu.4-1:latest

WORKDIR /root

COPY print.R /root/print.R

RUN apt-get update
RUN apt-get install gfortran -yy
