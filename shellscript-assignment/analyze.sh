#!/bin/bash

log_file="/home/access.log"

analyze_log() {
    echo "Analyzing log file: $log_file"
    
    # Extract IP addresses, request URLs, and error codes from the log file
    ip_addresses=$(awk '{print $1}' "$log_file")
    request_urls=$(awk '{print $7}' "$log_file")
    error_codes=$(awk '$9 ~ /^4|^5/ {print $9}' "$log_file")

    echo "Most frequent IP addresses:"
    echo "$ip_addresses" | sort | uniq -c | sort -nr | head -n 10
    
    echo "Most frequent request URLs:"
    echo "$request_urls" | sort | uniq -c | sort -nr | head -n 10

    echo "Occurrences of error codes:"
    echo "$error_codes" | sort | uniq -c
}

analyze_log
