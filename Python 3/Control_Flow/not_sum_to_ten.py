'''
1. Not Sum To Ten
To start, let’s check if the summation of two values does NOT equal ten.

You are given two numbers stored in num1 and num2. If the sum of num1 and num2 is NOT equal to 10, 
then store True into a variable called not_ten, 
otherwise store False in not_ten.

'''

num1 = 6
num2 = 3


# Write your if statement here
if num1 + num2 != 10:
  not_ten = True
else: 
  not_ten = False


# Uncomment the below lines to show the result
print("Is the sum of the numbers not equal to 10? " + str(not_ten))
