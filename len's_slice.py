#Len's Slice
# Your code below:

toppings = ["pepperoni" , "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

print("number of occurences of 2: " + str(num_two_dollar_slices))

num_pizzas = len(toppings)
print("lenth of the toppings list: " + str(num_pizzas))

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"] , [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

print(pizza_and_prices)

#Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending) number.
pizza_and_prices.sort()
print(pizza_and_prices)

#store the first element of the list after sorted
cheapest_pizza = pizza_and_prices[0]
print("cheapest pizza is " + str(cheapest_pizza))

# last item (most expensive) of the list 
priciest_pizza = pizza_and_prices[-1]
print("Most expensive pizza is " + str(priciest_pizza))

# remove the most expensive pizza from the list after the man bought it
pizza_and_prices.pop(-1)
print(pizza_and_prices)

#you want to add a new topping called "peppers"
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# first 3 cheapest pizza
# first 3 items in the list
# 3 in [:3] is number of element not index
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
