#!/bin/bash

who=$(whoami)
hostname=$(hostname)
kernel=$(uname -r)

array=( $who $hostname $kernel )
while true; do
    round=1
    for i in ${array[@]}; do
        echo $i
    done
    sleep 60
    
done