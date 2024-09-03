#Combining Lists: The Zip Function

'''
Combining Lists: The Zip Function
Learn about a popular Python built-in function called zip().

In Python, we have an assortment of built-in functions that allow us to build our programs faster and cleaner. One of those functions is zip().

The zip() function allows us to quickly combine associated data-sets without needing to rely on multi-dimensional lists. While zip() can work with many different scenarios, we are going to explore only a single one in this article.

Let’s use a list of student names and associated heights as our example data set:

Jenny is 61 inches tall
Alexus is 70 inches tall
Sam is 67 inches tall
Grace is 64 inches tall
Suppose that we already had a list of names and a list of heights:

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

If we wanted to create a nested list that paired each name with a height, we could use the built-in function zip().

The zip() function takes two (or more) lists as inputs and returns an object that contains a list of pairs. Each pair contains one element from each of the inputs. This is how we would do it for our names and heights lists:

names_and_heights = zip(names, heights)

If we were to then examine this new variable names_and_heights, we would find it looks a bit strange:

print(names_and_heights)

Would output:

<zip object at 0x7f1631e86b48>

This zip object contains the location of this variable in our computer’s memory. Don’t worry though, it is fairly simple to convert this object into a useable list by using the built-in function list():

converted_list = list(names_and_heights)
print(converted_list)

Outputs:

[('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]

Notice two things:

Our data set has been converted from a zip memory object to an actual list (denoted by [ ])

Our inner lists don’t use square brackets [ ] around the values. This is because they have been converted into tuples (an immutable type of list).

Let’s practice using zip()!

Coding question
Questions
Use zip() to create a new variable called names_and_dogs_names that combines owners and dogs_names lists into a zip object.

Then, create a new variable named list_of_names_and_dogs_names by calling the list() function on names_and_dogs_names.

Print list_of_names_and_dogs_names.
'''

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)

'''
OUTPUT

[('Jenny', 'Elphonse'), ('Alexus', 'Dr. Doggy DDS'), ('Sam', 'Carter'), ('Grace', 'Ralph')]


'''