#!/usr/bin/env python3

#########################################################################################################
###### This script will take the filename as arg and print the total number of lines in that file #######
#########################################################################################################
import sys

def line_count(filename):
#write the code for line_count function here
    try:
        with open(filename, 'r') as file:
            lines=sum(1 for line in file)
        return lines
    except FileNotFoundError:
        print(f"The mentioned file {filename} is missing!!!")
        sys.exit(1)

def main():
#write code for main 
    filename=sys.argv[1]
    line_count_value=line_count(filename)
    print(f"Total no. of line in {filename} are : " + str(line_count_value))

main()