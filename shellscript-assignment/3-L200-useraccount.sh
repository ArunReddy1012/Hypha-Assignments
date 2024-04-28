add_user(){
    #write the code for adding a new user here
    echo "Enter the username to create"
    read username
    useradd $username
    if [ $? -eq 0 ]; then
        echo "user $username is created successfully"
    else
        echo "Failed to create the user"
    fi
    read -p "Press Enter to continue or [CTRL + c] to exit"
}

modify_user() {
    #write the code for modifying the user here
    read -p "Enter username to modify: " username

    if id "$username" &>/dev/null; then

        read -p "Enter new full name: " new_full_name
        usermod -c "$new_full_name" "$username"

        if [ $? -eq 0 ]; then
            echo "User $username modified successfully."
        else
            echo "Failed to modify user $username."
        fi
    else
        echo "User $username does not exist."
    fi
    read -p "Press Enter to continue or [CTRL + c] to exit"
}

delete_user() {
    #write the code for deleteing the user here 
    read -p "Enter the valid userame to delete :" username

    if id $username &>/dev/null ; then
        userdel $username
        echo "user $username is deleted"
    else
        echo "INVALID !! user $username does not exist, please enter valid username"
    fi
    read -p "Press Enter to continue or [CTRL + c] to exit"
}

menu() {
    #write the menu function here
    echo "User Account Management"
    echo "1.Add user"
    echo "2.Modify user"
    echo "3.Delete user"
    echo "4.Exit"
    read -p "Enter your choice from the display :" choice
    case $choice in
        1) add_user ;;
        2) modify_user ;;
        3) delete_user;;
        4) exit;;
        *) echo "Invalid choice !!; sleep 2" 
    esac    
}

main() {
    
    while true; do
        menu
        sleep 2
    done
}

main