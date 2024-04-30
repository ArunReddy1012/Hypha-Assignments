# Using a list comprehension

#########################################################################################################
################ This script will calulate teh sqaue of a number using generator expression #############
#####################################    Author : Arun Reddy       ######################################
#########################################################################################################

squares_list = [x ** 2 for x in range(1, 21)]
print("List of squares (using list comprehension):", squares_list)

# Using a generator expression
squares_generator = (x ** 2 for x in range(1, 21))
print("List of squares (using generator expression):", end=" ")
for square in squares_generator:
    print(square, end=" ")
print()
