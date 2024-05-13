#!/bin/bash

audit_useraccounts(){

echo "Audit User Account : "
echo "==================================="
users=$(cat /etc/passwd)
echo "List of users : "
echo $users | awk -F: '{print "User : " ,$1, "Last Login : ", $6 }'

}

#audit_filepermissi(){
#
#}

main(){

    audit_useraccounts
    #audit_filepermissions

}


main
