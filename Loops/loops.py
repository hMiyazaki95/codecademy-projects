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


