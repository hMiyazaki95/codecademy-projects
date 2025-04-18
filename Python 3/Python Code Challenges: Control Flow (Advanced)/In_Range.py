'''
1. In Range
Let’s start the advanced challenge problems by testing if a number falls within a certain range. We will accept three parameters where the first parameter is the number we are testing, the second parameter is the lower bound and the third parameter is the upper bound of our range. These are the steps required:

Define the function to accept three numbers as parameters
Test if the number is greater than or equal to the lower bound and less than or equal to the upper bound
If this is true, return True, otherwise, return False

Create a function named in_range() that has three parameters named num, lower, and upper.

The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.
'''


# Write your in_range function here:
def in_range(num, lower, upper):
  if num >= lower & num <= upper:
    return True
  else:
    return False

# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False