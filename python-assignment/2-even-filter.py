#!/usr/bin/env python3

#########################################################################################################
###### This script will filter the given list of numbers and prints only the list of even numbers #######
#########################################################################################################

def filter_even_numbers():
    for num in random_list:
        if (num % 2 == 0) :
            even_list.append(num)
    return even_list

def main():
    random_list=[1,2,3,4,5,6,7,8,9,10]
    even_list=[]
    print("Even numbers list is : ",filter_even_numbers(random_list,even_list))

main()