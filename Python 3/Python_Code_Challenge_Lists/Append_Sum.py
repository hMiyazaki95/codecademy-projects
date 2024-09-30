'''
2. Append Sum
For the next challenge, let’s create a function that calculates the sum of the last two elements of an input list and appends it to the end of the original list. After doing so, it repeats this process two more times and returns the resulting list.

For example, for the input list [1, 1, 2], the output list should be [1, 1, 2, 3, 5, 8]. Similarly, the output for the input list [1, 23] should be [1, 23, 24, 47, 71].

To complete the challenge, you need to implement the following:

Define the function append_sum() to accept a list as its input argument.
Add the last and second-to-last elements of the input list.
Append the calculated sum to the end of the input list.
Repeat the previous two steps two more times for the modified list.
Return the modified list.
'''



# Write your function here

def append_sum(my_list):
  sum_of_last_two_elements = my_list[-1] + my_list[-2]
  my_list.append(sum_of_last_two_elements)
  sum_of_last_two_elements = my_list[-1] + my_list[-2]
  my_list.append(sum_of_last_two_elements)
  sum_of_last_two_elements = my_list[-1] + my_list[-2]
  my_list.append(sum_of_last_two_elements)
  
  return my_list


# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))


