# 1. Larger Sum
# We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which one has a greater sum. Here are the steps we need:

# Define the function to accept two input parameters: lst1 and lst2
# Create two variables to record the two sums
# Loop through the first list and add up all of the numbers
# Loop through the second list and add up all of the numbers
# Compare the first and second sum and return the list with the greater 



# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

# The function should return the list whose elements sum to the greater number. If the *********sum of the elements of each list are *********equal*********, return lst1.



#Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for i in lst1: # loop through the list of numbers
    sum1 += i # first sum1 = 1 # second time sum1 = 10 # third time sum1 = 15
  for i in lst2:
    sum2 += i # first sum2 = 2 # second time sum2 = 5 # third time sum2 = 12
  if sum1 >= sum2: # this worked 
    return lst1
  else:
    return lst2
  

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))