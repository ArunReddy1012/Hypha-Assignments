#!/bin/bash

audit_useraccounts(){

    echo "Audit User Account : "
    echo "==================================="
    users=$(lastlog)
    echo "List of users : "
    echo "$users" | awk -F: '{print "User : " ,$1 }'

}

audit_filepermissions(){
    echo "Audil File Permissions : "
    echo "===================================="
    directories=("/tmp", "/etc")
    for dir in $directories ; do
        echo "Directory : $dir "
        find $dir -type f -perm -o+w -exec ls -l {} +
        echo 
    done 


}

main(){

    audit_useraccounts
    audit_filepermissions

}


main
