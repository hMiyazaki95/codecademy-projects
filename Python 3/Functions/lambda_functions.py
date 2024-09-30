# Sample list of names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']


# Using map with a lambda function to get the length of each name
name_lengths = list(map(lambda x: len(x), names))


# Using map with a defined function to capitalize each name
def capitalize_name(name):
   return name.upper()


capitalized_names = list(map(capitalize_name, names))


# Print the results
print("Original names:", names)
print("Name lengths:", name_lengths)
print("Capitalized names:", capitalized_names)


# Try creating your own map function!
# Uncomment and modify the line below:
# your_result = list(map(lambda x: # Your function here, names))
# print("Your result:", your_result)


# x is the charactor list
#x[0] is the first charactor in the 'word'
# w
first_letters = list(map(lambda x: x[0], names))
print("First letters:", first_letters)


reversed_names = list(map(lambda x: x[::-1], names))
print("Reversed names:", reversed_names)




last_letters = list(map(lambda x: x[-1], names))
print("Last letters:", last_letters)
# Output: ['e', 'b', 'e', 'd', 'e']


name_length_check = list(map(lambda x: len(x) > 3, names))
print("Is name length > 3:", name_length_check)
# Output: [True, False, True, True, True]




name_initials = list(map(lambda x: x[0] + x[-1], names))
print("Name initials:", name_initials)
# Output: ['Ae', 'Bb', 'Ce', 'Dd', 'Ee']


vowel_count = list(map(lambda x: sum(1 for char in x if char.lower() in 'aeiou'), names))
print("Vowel count:", vowel_count)
# Output: [3, 1, 3, 2, 2]




doubled_letters = list(map(lambda x: ''.join([char * 2 for char in x]), names))
print("Doubled letters:", doubled_letters)
# Output: ['AAlliiccee', 'BBoobb', 'CChhaarrlliiee', 'DDaavviidd', 'EEvvee']




ascii_values = list(map(lambda x: ord(x[0]), names))
print("ASCII values of first letters:", ascii_values)
# Output: [65, 66, 67, 68, 69]




# Define a function to square a number
def square(x):
   return x ** 2


# List of numbers
numbers = [1, 2, 3, 4, 5]


# Use map() to apply the square function to each element in the list
squared_numbers = list(map(square, numbers))


# Print the result
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]






# Define a function to capitalize each name
def capitalize_name(name):
   return name.upper()


# List of names
names = ['Alice', 'Bob', 'Charlie']


# Use map() to apply the capitalize_name function to each name
capitalized_names = list(map(capitalize_name, names))


# Print the result
print(capitalized_names)
# Output: ['ALICE', 'BOB', 'CHARLIE']






# Define a function to add two numbers
def add(a, b):
   return a + b


# Two lists of numbers
list1 = [1, 2, 3]
list2 = [10, 20, 30]


# Use map() to add corresponding elements from both lists
result = list(map(add, list1, list2))


# Print the result
print(result)
# Output: [11, 22, 33]



