

encrypt_file() {
    #write the code for encrypting a file here

    read -p "Enter the AES-256-CBC encryption password " password
    read -p "Enter the file to encrypt" input_filename 
    read -p "Enter the output filename" output_filename
    if [ -f $input_filename ]; then
        openssl enc -aes-256-cbc -salt -in "$input_filename" -out "$output_filename" -pass pass:$password
        if [ $? -eq 0 ]; then
            echo "The file $input_filename has been encrypted and saved in $output_filename"
        fi 
    else 
        echo "The file $input_filename does not exist"
    fi
}

decrypt_file() {
    #write the code for decrypting a file here
    read -p "Enter the AES-256-CBC encryption password " password
    read -p "Enter the file to decrypt" input_filename 
    read -p "Enter the output filename" output_filename
    if [ -f $input_filename ]; then
        openssl enc -d -aes-256-cbc -in "$input_filename" -out "$output_filename" -pass pass:$password
        if [ $? -eq 0 ]; then
            echo "The file $input_filename has been decrypted and saved in $output_filename"
        fi
    else
        echo "The file $input_filename does not exist"
    fi 

}

echo "1.Encrypt a file"
echo "2.Decrypt a file"
read -p "choose the option here" choice

case $choice in 
    1) encrypt_file ;;
    2) decrypt_file ;;
    3) exit ;;
    *) echo "Invalid !! Please enter the valid selection"
esac


