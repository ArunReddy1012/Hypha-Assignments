#!/bin/bash

### Script to monitor the file modification ###

echo "Enter the file you want to monitor"

read file

initial_time=$(stat -c %Y "$file")

### checking if the file has actually modified or not ###

while true; do 
    current_time=$(date +"%Y-%m-%d %H:%M:%S")
    present_time=$(stat -c %Y $file)
    if [ $initial_time -ne $present_time ]; then
        echo " The file $file has been modified at $current_time" 
        initial_time=$current_time
    fi

    sleep 1
done
