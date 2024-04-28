#!/bin/bash
countdown() {
    seconds=$1
    while [ $seconds -gt 0 ] ; do 
        echo -ne "Time remaining: $seconds seconds\033[0K\r"
        sleep 1
        ((seconds--))
    done
    echo "Time is UP!!\n"
}

if [ $duration -lt 1 ]; then
    echo "ERROR, PLease enter number greater than 1"
    exit 1
fi

echo "Enter the duration for countdown"
read duration


countdown $duration