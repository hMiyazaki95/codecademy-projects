#Infinite Loops
'''
!!!!!!!!!!!!!!!!!!!!!!!!

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_A.append(student) # this is the line causing infinite loop
  print(student)

'''


#Loop Control: Break

'''
for item in items_on_sale:
  if item == "knit dress":
    print("Found it")

This code goes through each item in items_on_sale and checks for a match. This is all fine and dandy but what’s the downside?

Once "knit_dress" is found in the list items_on_sale, we don’t need to go through the rest of the items_on_sale list. Unfortunately, our loop will keep running until we reach the end of the list.

Since it’s only 5 elements long, iterating through the entire list is not a big deal in this case but what if items_on_sale had 1000 items? What if it had 100,000 items? This would be a huge waste of time for our program!

Thankfully you can stop iteration from inside the loop by using break loop control statement.

When the program hits a break statement it immediately terminates a loop. For example:

items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

print("Checking the sale list!")

for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break

print("End of search!")


'''




dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

'''
dog_breeds_available_for_adoption.

Using a for loop, iterate through the dog_breeds_available_for_adoption list and print() out each dog breed.

Use the <temporary variable> name of dog_breed in your loop declaration.
'''
for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  '''
  2.
    Inside your for loop, after you print each dog breed, check if the current element inside dog_breed is equal to dog_breed_I_want. If so, print "They have the dog I want!"
  '''
  if dog_breed == dog_breed_I_want:  
    print("They have the dog I want!")
    break
print(dog_breed)



#Loop Control: Continue

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

# The loop control statement called 'continue' can be used to skip certain groups of data types or numbers (e.g., negative or positive numbers) based on the condition specified in the if statement.

'''
for i in big_number_list:
  if i <= 0: # ignore 0 and negative
    continue # search till end of the list by skipping 0 and negative
  print(i)
'''

for i in ages:
  if i < 21:
    continue
  print(i)
  
  
  
#Nested Loop


'''
Loops can be nested in Python, as they can with other programming languages. We will find certain situations that require nested loops.

Suppose we are in charge of a science class, that is split into three project teams:

project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

Using a for or while loop can be useful here to get each team:

for team in project_teams:
  print(team)

Would output:

["Ava", "Samantha", "James"]
["Lucille", "Zed"]
["Edgar", "Gabriel"]

But what if we wanted to print each individual student? In this case, we would actually need to nest our loops to be able to loop through each sub-list. Here is what it would look like:

# Loop through each sublist
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)

This would output:

Ava
Samantha
James
Lucille
Zed
Edgar
Gabriel

'''

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0
for location in sales_data:
  print(location)
  for scoops in location:
    scoops_sold += scoops
print(scoops_sold)



#List Comprehensions: Introduction


'''

To start, let’s say we had a list of integers and wanted to create a list where each element is doubled. We could accomplish this using a for loop and a new list called doubled:

numbers = [2, -1, 79, 33, -45]
#providing empty list for doubled list
doubled = []

for number in numbers:
  doubled.append(number * 2)

print(doubled)

Output:
[4, -2, 158, 66, -90]

Let’s see how we can use the power of list comprehensions to solve these types of problems in one line. Here is our same problem but now written as a list comprehension:

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)

et’s break down our example in a more general way:

new_list = [<expression> for <element> in <collection>]


In our doubled example, our list comprehension:

Takes an element in the list numbers
Assigns that element to a variable called num (our <element>)
Applies the <expression> on the element stored in num and adds the result to a new list called doubled
Repeats steps 1-3 for every other element in the numbers list (our <collection>)

'''


grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades] #elegant loop

print(scaled_grades)






#List Comprehensions: Conditionals


'''We will start by using a for loop and a list only_negative_doubled:

numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)

print(only_negative_doubled) 

Would output:

[-2, -90]

Now, here is what our code would look like using a list comprehension:

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

Would output the same result:

[-2, -90]

In our negative_doubled example, our list comprehension:

Takes an element in the list numbers.
Assigns that element to a variable called num.
Checks if the condition num < 0 is met by the element stored in num. If so, it goes to step 4, otherwise it skips it and goes to the next element in the list.
Applies the expression num * 2 on the element stored in num and adds the result to a new list called negative_doubled
Repeats steps 1-3 (and sometimes 4) for each remaining element in the numbers list.
'''






# We have defined a list heights of visitors to a theme park. In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters. 
# Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
# Print can_ride_coaster.
can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)



'''
Loops Review

How to write a for loop.
How to use range in a loop.
How to write a while loop.
What infinite loops are and how to avoid them.
How to control loops using break and continue.
How to write elegant loops as list comprehensions.
'''

# Your code below:

# Create a list called single_digits that consists of the numbers 0-9 (inclusive).

single_digits = range(10)

# Before the loop, create a list called squares. Assign it to be an empty list to begin with.

squares = []

#Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.
cubes = []

# Create a for loop that goes through single_digits and prints out each one.
for num in single_digits:
  # Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.
  squares.append(num ** 2)
  cubes.append(num ** 3)
# After the for loop, print out squares.
print(squares)
print(cubes)



# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]





# 


