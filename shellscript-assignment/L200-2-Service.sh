check_status() {
# check the status here
    if systemctl is-active --quiet "$1"; then
        return 0
    else
        return 1
    fi
}

log_message() {
# write the logs for failed service here
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> /var/log/service.log
}

restart_service() {
# restart the service here 
    systemctl restart "$1"
    if [ $? -eq 0 ]; then
        log_message "$1 is restarted....."
    fi
}

restart() {
    while true; do 
        for service in "${list_services[@]}"; do 
            if ! check_status "$service"; then
                log_message "$service service is down, restarting......."
                restart_service "$service"
            fi
        done
        sleep 30
    done
}

list_services=("httpd" "nginx")

restart