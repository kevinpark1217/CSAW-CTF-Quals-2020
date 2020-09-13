FROM amd64/ubuntu:18.04

WORKDIR /chal

RUN apt-get update && apt-get -y install gdb netcat
EXPOSE 1234 4444

COPY grid binary
COPY libc-2.27.so libc
COPY libstdc.so.6.0.25 libstdc

RUN chmod +x *

COPY docker_* ./
RUN chmod +x docker_*
CMD ["./docker_nc.sh"]
