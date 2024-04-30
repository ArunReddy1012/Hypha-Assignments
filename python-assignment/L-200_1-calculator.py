#!/usr/bin/env python3

#########################################################################################################
######################## This script will perfom simple calculator operations ###########################
#########################################################################################################


def addition(a,b):
    try:
        print(a+b)
    except ValueError:
      print("The entered value is not a number, please make a valid entry")  

def substraction(a,b):
    try:
        print(a-b)
    except ValueError:
      print("The entered value is not a number, please make a valid entry")

def multiplication(a,b):
    try:
        print(a*b)
    except ValueError:
      print("The entered value is not a number, please make a valid entry")

def division (a,b):
    try:
        print(a/b)
    except ValueError:
      print("The entered value is not a number, please make a valid entry")
    except ZeroDivisionError:
      print("You are trying to divide a number with 0, which is incorrect!!")    

def switchcase(choice,a,b):
    match choice:
        case "1":
            result=addition(a,b)
        case "2":
            result=substraction(a,b)
        case "3":
            result=multiplication(a,b)
        case "4":
            result=division(a,b)
    
def main():

    a=float(input("Enter the value of num1 : "))
    b=float(input("Enter the value of num2 : "))

    print("Enter the number of your choice from the below operations :\n")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

    user_input=input("")
    switchcase(user_input,a,b)

main()