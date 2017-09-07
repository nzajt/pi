#!/bin/bash
PIPID=$(ps aux | grep python | awk '{print $2}')
echo $PIPID 
kill -9 $PIPID
PORTS=(17 22 24)
for port in $PORTS; do
  echo $port
  pigs p $port 0
done
