FROM amd64/ubuntu:18.04

WORKDIR /chal

RUN apt-get update && apt-get -y install gdb netcat
EXPOSE 1234 4444

COPY bard binary
COPY libc-2.27.so libc

RUN chmod +x *

COPY docker_* ./
RUN chmod +x docker_*
CMD ["./docker_nc.sh"]

