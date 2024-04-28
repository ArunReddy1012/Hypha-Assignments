#!/usr/bin/env python3

import random

#########################################################################################################
################ This script will responds based on the user input from the match-case ##################
#########################################################################################################
def process_function(choice):
    match choice:
        case "START":
            print("Starting the random numbers display", print(random.randint(0,9)))
        case "STOP":
            print("Stopping the process")
        case "EXIT":
            print("Exiting the process", exit())
        case _:
            print("Please make a valid choice")

def main():
    user_input=print("Enter the choice (1.START , 2.STOP , 3.EXIT):")
    A=process_function(user_input)

main()

