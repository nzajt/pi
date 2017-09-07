#!/bin/zsh
kill -9 $(ps aux | grep python | awk '{print $2}')
PORTS=(17 22 24)
for port in $PORTS; do
  pigs p $port 0
done
