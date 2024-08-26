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
