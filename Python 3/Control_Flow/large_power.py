'''
3. Large Power
For the next code challenge, let’s add functions to the mix! We create a function that tests whether the result of taking the power of one number to another number provides an answer that is greater than 5000. We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. In order to accomplish this, we will need the following steps:

Define the function to accept two input parameters called base and exponent
Calculate the result of base to the power of exponent
Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False
'''


'''
Create a function named large_power() that takes two parameters named base and exponent.

If base raised to the exponent is greater than 5000, return True, otherwise return False

''' 
# Write your large_power function here:

def large_power(base, exponents):
  if base ** exponents > 5000:
    return True
  else: 
    return False

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
#