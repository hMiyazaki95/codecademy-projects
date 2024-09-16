'''
Python List Methods

.count() - A list method to count the number of occurrences of an element in a list.

.insert() - A list method to insert an element into a specific index of a list.

.pop() - A list method to remove an element from a specific index or from the end of a list.

range() - A built-in Python function to create a sequence of integers.

len() - A built-in Python function to get the length of a list.

.sort() / sorted() - A method and a built-in function to sort a list.


Add and remove items from a list using a specific index.
Create lists with continuous values.
Get the length of a list.
Select portions of a list (called slicing).
Count the number of times that an element appears in a list.
Sort a list of items.




# Example syntax for methods
list.method(input)

# Example syntax for a built-in function 
builtinfunction(input)

'''

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 

#.inesrt()
#The index you want to insert into.
#The element you want to insert at the specified index.
##store_line.insert(2, "Vikor")
#print(store_line) 
front_display_list.insert(0, "Pineapple")

#Removing by Index: Pop
#The pop() function removes the last element or the element based on the index given. remove() function removes the first occurrence of the specified element.

#example 
'''
removed_element = cs_topics.pop()
print(cs_topics)
print(removed_element)
'''



#Removing by Index: Pop

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 
#The pop() function removes the last element or the element based on the index given. 
#remove() function removes the first occurrence of the specified element.

#remove the topic Python 3
data_science_topics.pop()
print(data_science_topics)

#remove the element at index 3
data_science_topics.pop(3)
print(data_science_topics)


#Consecutive Lists: Range

#range()
# generate number from 0
# generate number until before the number that's in the range(). 
#range(20) this provie the number from 0 - 19

# Your code below: 

# numbers 0 and up to, but not including 9
number_list = range(9)
print(list(number_list))

#numbers 0 through 7.
zero_to_seven = range(0, 8)
print(list(zero_to_seven))


#The Power of Range!

# Your code below: 

# Starts at 5
# Has a difference of 3 between each item
# Ends before 15
range_five_three = range(5, 15, 3)
print(list(range_five_three))



#Length

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# slice the element at index 4 and after show elements from index 0 through 3
#the first 2 elements of suitcase
beginning = suitcase[0:2]

# Your code below: 

print(beginning)

middle = suitcase[2:4]

print(middle)

#Slicing Lists II



# Starts at 0
# Has a difference of 5 between each item
# Ends before 40
range_diff_five = range(0, 40, 5)
print(list(range_diff_five))
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
# Your code below: 
# Calculate the length of long_list
long_list_len = len(long_list)
print(long_list_len)



#hange the range() function that generates big_range so that it skips 100 instead of 10 steps between items.
big_range = range(2, 3000, 10)
# calculate the length of big_range
big_range_length = len(big_range)
print(big_range_length)




'''
Example

fruits = ["apple", "cherry", "pineapple", "orange", "mango"]

# select the first n elements of a list
fruits[:n]

# slicing index from 0 to up to 3 but the element at the index 3 is not included
print(fruits[:3])

# slice last n element
fruits[-n:]

#slices from the element at index -2
print(fruits[-2:])

#taking sll the element except last element in the list
fruits[:-n]

# 0 ~ -1 last element
print(fruits[:-1])


'''


suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
# last 2 elements without first 4 elements
last_two_elements = suitcase[-2:]
print(last_two_elements)

#containing all except last three element
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)


# Counting in a List

'''
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
# count how many letter 'i' in the list 
num_i = letters.count("i")
print(num_i)

# number collection 2D list
number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]

# count how many sublist in the list appeares 
num_pairs = number_collection.count([100, 200])
print(num_pairs)

'''


votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count("Jake")
print(jake_votes)



#Sorting Lists 1

'''
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

# sort the list in the Alphabetical order
names.sort()
print(names)

'''

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]

addresses.sort()
print(addresses)


# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
#.sort() call on cities such that it sorts the cities in reverse order (descending).
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)



#Sorting Lists II
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
# sorted Alphabetically
games_sorted = sorted(games)
print(games) #not sorted
print(games_sorted) # soted in assending order

#Review

'''
# List methods
In this lesson, we learned how to:

Add elements to a list by index using the .insert() method.

Remove elements from a list by index using the .pop() method.

Generate a list using the range() function.

Get the length of a list using the len() function.

Select portions of a list using slicing syntax.

Count the number of times that an element appears in a list using the .count() method.

Sort a list of items using either the .sort() method or sorted() function.

'''

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# how many items are in the warehouse?
inventory_len = len(inventory)
print(inventory_len)
# first element in inventory
first = inventory[0]
print(first)
# lasg element in the inventory
last = inventory[-1]
print(last)
# items from the inventory starting at index 2 and up to, but not including, index 6.
inventory_2_6 = inventory[2:6]
print(inventory_2_6)
# first 3 items of inventory
first_3 = inventory[0:3]
print(first_3)
#How many "twin bed"s are in inventory
twin_beds = inventory.count("twin bed")
print(twin_beds)
#remove the 5th element in the inventory
removed_item = inventory.pop(4)
print(removed_item)
# add the new item to an inventory as 11th item
inventory.insert(10, "19th Century Bed Frame")
# sort inventory
inventory.sort()
print(inventory)
inventory_sorted = sorted(inventory)
print(inventory_sorted)
