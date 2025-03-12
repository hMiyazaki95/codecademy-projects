# 2. Greetings
# You are invited to a social gathering, but you are tired of greeting everyone there. Luckily we can create a function to accomplish this task for us. In this challenge, we will take a list of names and prepend the string 'Hello, ' before each name. This will require a few steps:

# Define the function to accept a list of strings as a single parameter called names
# Create a new list of strings
# Loop through each name in names
# Within the loop, concatenate 'Hello, ' and the current name together and append this new string to the new list of strings
# Afterwards, return the new list of strings


# Create a function named add_greetings() which takes a list of strings named names as a parameter.

# In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.

# Return the new list containing the greetings.


#Write your function here
'''
Define the function to accept a list of strings as a single parameter called names
Create a new list of strings
Loop through each name in names
Within the loop, concatenate 'Hello, ' and the current name together and append this new string to the new list of strings
Afterwards, return the new list of strings

Create a function named add_greetings() which takes a list of strings named names as a parameter.

In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.

Return the new list containing the greetings.
'''

def add_greetings(names):
  new_names_list = [] # create empty list
  for name in names: #iterates through the list
    new_names_list.append('Hello, ' + name)
  return new_names_list


#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

# output ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']