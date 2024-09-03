# While Loops: Introduction
'''
while <conditional statement>:
  <action>

count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1


Indentation:

Notice that in our example the code under the loop declaration is indented. Similar to a for loop, everything at the same level of indentation after the while loop declaration is run on every iteration of the loop while the condition is true.

while count <= 3:
   # Loop Body
   print(count)
   count += 1
   # Any other code at this level of indentation will
   # run on each iteration



Elegant loops:
Similar to for loops, Python allows us to write elegant one-line while loops. Here is our previous example in a single line:

count = 0
while count <= 3: print(count); count += 1

'''




# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# Your code below: 

#a while loop that counts down from 10 to 0(inclusive). Once our loop is finished we will commemorate our accomplishment by printing "We have liftoff!".

countdown = 10
print("Starting While Loop")
while countdown >= 0:
  #print() the value of the countdown variable.
  print(countdown)
  # decrease the value of the countdown variable by 1
  countdown -= 1
#commemorate our success
print("We have liftoff!")  


'''
countdown = 10
print("Starting While Loop")
while countdown >= 0:
  print("We have liftoff!" + str(countdown))
  countdown -= 1
print("While Loop ended")
'''

# While Loops: Lists

'''
length = len(ingredients)
index = 0

while index < length:
  print(ingredients[index])
  index += 1
'''
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
# this provide length 6
# len provide the number of element, which is the length of the list
length = len(python_topics)
index = 0
# length - 1 is the number of index in the list so that the condition will be index is less than length
while index < length:
  print("I am learning about " + python_topics[index])
  index += 1

#Infinite Loops
'''
!!!!!!!!!!!!!!!!!!!!!!!!

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_A.append(student) # this is the line causing infinite loop
  print(student)

'''



