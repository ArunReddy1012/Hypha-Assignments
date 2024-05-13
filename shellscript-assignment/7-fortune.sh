#!/bin/bash

# Define an array of fortune messages
fortunes=(
    "You will find success in unexpected places."
    "Good things will come to you when you least expect them."
    "A smile is your passport into the hearts of others."
    "The road to success is always under construction."
    "The best way to predict the future is to create it."
    "Your hard work will pay off soon."
    "You are destined for greatness."
    "Opportunities are all around you."
)

while true; do
    index=$((RANDOM % ${#fortunes[@]}))

    fortune=${fortunes[index]}

    echo "Your fortune is: $fortune"

    sleep 5
done
