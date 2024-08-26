example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
# print(example_list)

#Using Remove
example_list.remove(5)
# print(example_list)


orders = ["daisies", "periwinkle"]
orders.append("tulips")
orders.append("roses")
print(orders)


orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = orders + ["lilac", "iris"]
# combine orders
orders_combined = orders + new_orders


broken_prices = [5, 3, 4, 5, 4] + [4]




employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

#inside the array is index
employee_four = (employees[3])

# this cause error because there is no element in the index 8
#print(employees[8])




shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

#how to access the last element in the list
last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(last_element + " = " + index5_element)


# Your code below:
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

#replacing the element in the specific index with new element
garden_waitlist[1] = "Calla"
print(garden_waitlist)

#replacing last element with new element
garden_waitlist[-1] = "Alex"
print(garden_waitlist)




# Your code below: 
order_list =["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)

order_list.remove("Flatbread")
print(order_list)


new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)

new_store_order_list.remove("Mango")

print(new_store_order_list)

# this cause error because Onion doesn't exist
new_store_order_list.remove("Onion")







# 2D Lists

# first 2D list
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]


heights.append(["Vik", 68])
print(heights)

# second 2D list
ages = [["Aaron", 15],["Dhruti", 16]]

print(heights)

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]


#Your code below:
heights.append(["Vik", 68])
print(heights)

ages = [["Aaron", 15],["Dhruti", 16]]

print(heights)

####################################
'''
#Outermost "container" list
example_2d_list = [
  #Innermost sublists
  ["First Sublist", "Second Item"], 
  ["Second Sublist", "Second Item"], 
  ["Third Sublist", "Second Item"]
]
'''
######################################

#Your code below:

# creating 2D Lists to represent class room test score data
class_name_test = [["Jenny", 90], ["Alexus", 85.5] ,["Sam", 83], ["Ellie", 101.5]]

print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

#########################################
'''
Element	Access Index
"Second Item"	example_2d_list[-3][-1]
"Second Item Two"	example_2d_list[-2][-1]
"Second Item Three"	example_2d_list[-1][-1]
'''
##########################################




#Your code below:
#Modifying 2D Lists

##########################################
'''
Row (Sublist)	Column 0	            Column 1	           Column 2
Row 0	        [0][0] - "Kenny"	[0][1] - "American"	    [0][2] - 9
Row 1	        [1][0] - "Tanya"	[1][1] - "Ukrainian"	[1][2] - 9
Row 2           [2][0] - "Madison"	[2][1] - "Indian"	    [2][2] - 7

negative indices

Row (Sublist)	Column 0	            Column 1	            Column 2
Row -3	    [-3][0] - "Kenny"	    [-3][1] - "American"	[-3][2] - 9
Row -2	    [-2][0] - "Tanya"	    [-2][1] - "Ukrainian"	[-2][2] - 9
Row -1	    [-1][0] - "Madison"	    [-1][1] - "Indian"	    [-1][2] - 7




'''
##########################################
#create a list
incoming_class = [["Kenny",	"American",	9], ["Tanya",	"Ukrainian",	9], ["Madison",	"Indian",	7]]
print(incoming_class)

#modifying the elements in the list
#The grade is an element within each sublist, and its index is 2 within that sublist, but it’s not an index itself; it's the value at that index.

incoming_class[2][2] = 8
print(incoming_class)

incoming_class[-3][-3] = "Ken"
print(incoming_class)




# Your code below: 

'''
Review
19 min
So far, we have learned:

How to create a list
How to access, add, remove, and modify list elements
How to create a two-dimensional list
How to access and modify two-dimensional list elements
'''

first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]

#add another size for Depak
preferred_size.append("Medium")
print(preferred_size)

customer_data = [["Ainsley",	"Small",	True],["Ben",	"Large",	False],["Chani",	"Medium",	True],["Depak",	"Medium",	False]]

print(customer_data)

#change the boolean value for Chani
customer_data[2][2] = False
print(customer_data)

#delete the boolean value for the Ben
# first select the indices of row 
# add what atribute you want to remove in the remove dictionary
customer_data[1].remove(False)
print(customer_data)

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]

print(customer_data_final)



####################################################################

'''
How would you properly modify the list interview_line to replace "Ben" with "Sarah"

interview_line = ["Jess", "Noelle", "Ben", "Orlando"]

Your correct answer
interview_line[
2
] = 
"Sarah"

2.
Modify the two-dimensional list student_hobbies so that "Samantha" has the hobby of "Football" instead of "Cricket".

student_hobbies = [["Nitaya", "Karate"], ["Samantha", "Cricket"], ["Noelle", "Painting"]]

Your correct answer
student_hobbies
[
1
][
1
] = 
"Football"

3.
The Python method .remove() will delete every instance of a provided value.

Your correct answer
False

4.
What would be the proper way to access "Strawberry" from the list groceries

groceries = ["Grapes", "Strawberry", "Starfruit", "Apple"]
Your correct answer
groceries[1]

5.
Define a two-dimensional list called student_data using the table below to represent student names and their respective quiz scores.

The order of elements should be ordered using the index in the table.

Element	Index
[“Olga”, 90]	0
[“Maksim”, 77.45]	1
[“Doug”, 80.3]	2
[“Sophie”, 87.45]	3

Your correct answer
student_data
 = [
["Olga", 90]
, 
["Maksim", 77.45]
, 
["Doug", 80.3]
, 
["Sophie", 87.45]
]
6.
Which of the following is the correct way to remove the first instance of “Rio” from name_list?

Your correct answer
name_list.remove("Rio")

7.
How would you access "77.45" from the following list?

student_data = [["Ali", 90], ["Bob", 87.5], ["Cam", 80.3], ["Doug", 77.45]]

Your correct answer
student_data[-1][-1]

8.
Which of the following is the correct way to turn the following into a list of names: "Tom", "Jerry", "Tweetie", "Sylvester"?

Your correct answer
names = ["Tom", "Jerry", "Tweetie", "Sylvester"]

9.
Which of the following is the correct way to create an empty list?

Your correct answer
empty_list = []

10.
Is the following list a valid Python list?

mylist = ["Mount Everest", 29029]
Your correct answer
Yes, lists can contain multiple data types.

11.
Which of the following is the correct way to add the number 4 to number_list?

Your correct answer

'''