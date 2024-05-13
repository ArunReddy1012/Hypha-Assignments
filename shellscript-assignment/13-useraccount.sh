#!/bin/bash

audit_useraccounts(){

echo "Audit User Account : "
echo "==================================="
users=$(lastlog)
echo "List of users : "
echo "$users" | awk -F: '{print "User : " ,$1, "         Last Login : ", $4, $5, $6, $7 }'

}

#audit_filepermissi(){
#
#}

main(){

    audit_useraccounts
    #audit_filepermissions

}


main
