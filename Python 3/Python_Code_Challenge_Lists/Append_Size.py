'''
Challenges
We’ve included 5 list challenges below. Try to answer all of them and polish up your problem-solving skills and your list expertise.

1. Append Size
For the first code challenge, we are going to calculate the length of an input list and append it to the end of the original list. For example, if we have the input list [23, 42, 108], which is of length 3, the output list should be [23, 42, 108, 3]. Similarly, the output for the input list [1, 23] should be [1, 23, 2].

Here is what you need to do:

Define a function append_size() that accepts a list as its input.
Get the length of the input list.
Append the length of the list to the end of the original list.
Return the modified list.


Create a function called append_size() that has one parameter named my_list.

The function should append the size of my_list (inclusive) to the end of my_list. The function should then return this new list.

For example, if my_list was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of my_list was originally 3.

'''

# Write your function here
def append_size(my_list):
  # we need to find the length of the list first
  length = len(my_list)
  # append new element in the existing list
  my_list.append(length)
  return my_list

# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

