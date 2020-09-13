#!/bin/sh

for i in $(seq 2 255); do
	./turner -server web.chal.csaw.io:3478 2>&1 | grep channel &
	A=$!
	sleep 0.25
	proxychains curl 172.17.0.$i:5000
	kill $A &>/dev/null
	sleep 0.25
done
