# 3. Delete Starting Even Numbers
# Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements. It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed. To do this, we will need the following steps:

# Define our function to accept a single input parameter my_list which is a list of numbers
# Loop through every number in the list if there are still numbers in the list and if we haven’t hit an odd number yet
# Within the loop, if the first number in the list is even, then remove the first number of the list
# Once we hit an odd number or we run out of numbers, return the modified list


# Write a function called delete_starting_evens() that has a parameter named my_list.

# The function should remove elements from the front of my_list until the front of the list is not even. The function should then return my_list.

# For example if my_list started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(my_list) should return [11, 12, 15].

# Make sure your function works even if every element in the list is even!

#Write your function here
def delete_starting_evens(my_list):
    # Use a while loop to remove elements from the front
    # while length of array is greater than 0 and the list
    # And the my_list[0] % 2 == 0:to check if the first element of the list is an even number.  
    while len(my_list) > 0 and my_list[0] % 2 == 0:
        # Remove the first element if it's even
        my_list.pop(0)
        # return the list after the list even numbers are removed.
    return my_list
      

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


# output: [11, 12, 15]
# []