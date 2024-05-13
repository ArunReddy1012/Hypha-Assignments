#!/usr/bin/env/ python3

#########################################################################################################
############################## This script will perfom exception handling ###############################
#####################################    Author : Arun Reddy       ######################################
#########################################################################################################

def division_function(a,b):
   try:
      c=(a/b)
      return c
   except ValueError:
      print("The entered value is not of number, please make a valid entry")
   except ZeroDivisionError:
      print("You are trying to divide a number with 0, which is incorrect!!")    

def main():
   a=float(input("Enter the value of a : ")) 
   b=float(input("Enter the value of b : ")) 
   result=division_function(a,b)
   print(f"{a}/{b} is : ",result)

main()