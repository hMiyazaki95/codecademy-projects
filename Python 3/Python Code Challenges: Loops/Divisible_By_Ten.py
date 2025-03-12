# 1. Divisible By Ten
# Let’s start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers. This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number is divisible by 10, a counter will be incremented and the final count will be returned. These are the steps we need to complete this:

# Define the function to accept one input parameter called nums
# Initialize a counter to 0
# Loop through every number in nums
# Within the loop, if any of the numbers are divisible by 10, increment our counter
# Return the final counter value

#Write your function here
def divisible_by_ten(nums):
  count = 0
  for i in nums:  # nums is a list
    if i % 10 == 0:
        count += 1
  return count

     

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))


# output 3

