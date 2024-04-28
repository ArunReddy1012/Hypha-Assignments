#!/bin/bash

echo "Enter your name Please"

read name

while true; do

    TIME=$(date +"%A, %d %B %Y %I:%M %p")

    echo "Good day, $name!, Now the time is $TIME"

    sleep 5 
done