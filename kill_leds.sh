#!/bin/zsh
PIPID=$(ps aux | grep python | awk '{print $2}')
kill -9 $PIPID >/dev/null 2>&1
PORTS=(17 22 24)
for port in $PORTS; do
  pigs p $port 0
done
