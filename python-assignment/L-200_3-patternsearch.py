#########################################################################################################
######################## This script will perfom pattern searching in files #############################
#####################################    Author : Arun Reddy       ######################################
#########################################################################################################


import os

def search_string_in_files(directory, search_string):
    try:
        files = os.listdir(directory)

        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(directory, file_name)
                try:
                    with open(file_path, 'r') as file:
                        contents = file.read()
                        if search_string in contents:
                            print(f"Found '{search_string}' in file: {file_name}")
                except Exception as e:
                    print(f"Error reading file '{file_name}': {e}")
    except Exception as e:
        print(f"Error accessing directory '{directory}': {e}")

def main():
    directory = input("Enter the directory path: ")    #/home/arun/file1.txt
    search_string = input("Enter the string to search: ")

    search_string_in_files(directory, search_string)

main()
