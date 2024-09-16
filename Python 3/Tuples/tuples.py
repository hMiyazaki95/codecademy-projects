
# 4 items in the tuple
my_tuple = ('abc', 123, 'def', 456)

# the comma is required to hold the one item
my_tuple = ('abc',)


#Tuple Indexing and Slicing
my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

# items in tuple can be accessed with index
print(my_tuple[0]) # prints abc

#applying slicing in the tuple using range of indices to access multiple items
print(my_tuple[3:5]) # prints (456, 789)

#Common Built-in Functions

#len() helps count the items in the tuple
my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')
print(len(my_tuple)) # prints 6

#max()
# find the largest number in the tuple
my_tuple = (65, 2, 88, 101, 25)
max(my_tuple) # returns 101

'''
"o" in "orange" has a Unicode value of 111.
"b" in "blue" has a Unicode value of 98.
"r" in "red" has a Unicode value of 114.
"g" in "green" has a Unicode value of 103.
'''
# find the max of
my_tuple = ('orange', 'blue', 'red', 'green')
max(my_tuple) # returns "red"

# error
my_tuple = ('abc', 234, 567, 'def')
max(my_tuple) # throws an error!

#min()
my_tuple = (65, 2, 88, 101, 25)
min(my_tuple) # returns 2
my_tuple = ('orange', 'blue', 'red', 'green')
min(my_tuple) # returns "blue"
my_tuple = ('abc', 234, 567, 'def')
min(my_tuple) # throws an error!

#.index()
my_tuple = ('abc', 234, 567, 'def')
my_tuple.index('abc') # returns 0
my_tuple.index(567) # returns 2

#.count()
my_tuple = ('abc', 'abc', 2, 3, 4)
my_tuple.count('abc') # returns 2
my_tuple.count(3) # returns 1

# Example
my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

print(my_tuple[0])
print(my_tuple[3:5])

print(len(my_tuple)) 

print(my_tuple.index('abc'))
print(my_tuple.index(789)) 

