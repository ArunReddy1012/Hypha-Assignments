#!/usr/bin/env python3


def line_count(filename):
#write the code for line_count function here
    try:
        with open(filename, 'r') as file
        readlines=file.readlines()
        print(readlines)
        lines=len(file.readlines())
        return lines
    except Filenotfounderror:
        print("The mentioned file {filename} is missing!!!")
        sys.exit(1)

def main():
#write code for main 
    filename=sys.argv[0]
    line_count=line_count(filename)
    print("Total no. of line in {filename} are : " + str(line_count))

main()