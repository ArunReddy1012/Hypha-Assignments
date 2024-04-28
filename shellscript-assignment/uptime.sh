#!/bin/bash
echo "Please enter your name"

read user

echo "Hello $user, The system is in upstate from past:"

while true; do
    uptime

    sleep 5
done