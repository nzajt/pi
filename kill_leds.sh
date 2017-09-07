#!/bin/bash
PIPID=$(ps aux | grep python | awk '{print $2}')
echo $PIPID 
kill -9 $PIPID
ports=( 17, 22, 24 )
for port in "${array[@]}"
do
  echo $port
  pigs p ${port} 0
done
