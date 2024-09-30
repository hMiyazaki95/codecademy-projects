'''
5. Max Number
For the final challenge, we are going to select which number from three input values is the greatest using conditional statements. To do this, we need to check the different combinations of values to see which number is greater than the other two. Here is what we need to do:

Define a function that has three input parameters, num1, num2, and num3
Test if num1 is greater than the other two numbers
If so, return num1
Test if num2 is greater than the other two numbers
If so, return num2
Test if num3 is greater than the other two numbers
If so, return num3
If there was a tie between the two largest numbers, then return "It's a tie!"


Questions
Create a function called max_num() that has three parameters named num1, num2, and num3.

The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".


'''


# Write your max_num function here:
def max_num(num1, num2, num3):
  #create list with elements (nums)
  nums = [num1, num2, num3]
  # sort the numbers in ascending order
  sorted_nums = sorted(nums)
  # -1 returns last element in the sorted list which is largest number of the list
  if sorted_nums[-1] == sorted_nums[-2]:
    return "It's a tie!"
  # return largest number
  return sorted_nums[-1]
  
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
