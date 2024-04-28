
ip_list=("facebook.com" "google.com" "10.1.7.121" "amazon.com")

email_id="earun333@gmail.com"

send_alert () {
        local_target=$1
        echo "Ping to $i failed. Please check network health." | mail -s "Network Health Alert" "$email_id"

}

for i in ${ip_list[@]}; do
    ping -c 1 $i
    if [ $? -eq 0 ]; then
        echo "###################### Ping for $i is successfull #####################" 
    else
        echo "###################### Ping for $i is failed      #####################"
        echo "$(date '+%Y-%m-%d %H:%M:%S'): ping for $i is failed" >> /home/log_file.log
        send_alert $i
    fi
done
