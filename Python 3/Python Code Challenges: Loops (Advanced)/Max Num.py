# Max Num
# Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of numbers. This can be accomplished using the max() function in python, but as a challenge, we are going to manually implement this function. Here is what we need to do:

# Define the function to accept a list of numbers called nums
# Set our default maximum value to be the first element in the list
# Loop through every number in the list of numbers
# Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
# Return the maximum number

# Create a function named max_num() that takes a list of numbers named nums as a parameter.

# The function should return the largest number in nums


# Hint
# Create a variable called maximum to track the max number, and have it start as the first element in the list. Loop through all of the numbers in the list, and if a number is ever greater than the current max number, the max number should be re-set to that number.#Write your function here
def max_num(nums):
  maximum = nums[0]
  for num in nums: 
    if num > maximum:
      maximum = num
  return maximum
#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

# output 75