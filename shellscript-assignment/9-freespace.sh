#!/bin/bash

freespace() {
    dir=$1
    while true; do
        free_space=$(df -B1 $dir | awk 'NR==2 {print $4}')
        free_space_val=$(( free_space / 1024**3 ))
        echo " The free disk space is : $free_space_val GB"
        sleep 10
    done

}
echo "Please enter the path of the directory"
read path

freespace $path
