#!/bin/bash
kill -9 $(ps aux | grep python | awk '{print $2}')
ports=( 17 22 24 )
for port in "${array[@]}"
do
  pigs p ${port} 0
done
