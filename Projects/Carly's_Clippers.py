hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Task 1
total_price = 0

# Task 2
for price in prices:
    total_price += price

# Task 3
average_price = total_price / len(prices)
# Task 4
print("Average Haircut Price: ", average_price)

# Task 5
new_prices = price - 5
# Task 6
print("new prices are: ", new_prices)

# Task 7
total_revenue = 0

#Task 8
for i in range(len(hairstyles)):
  #Task 9Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: ", total_revenue)

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: ", average_daily_revenue)

# Carly wants to advertise haircuts that are under $30.
# Let's assume that `new_prices` are the same as `prices` for now.
new_prices = prices

# Task 12
# Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.
# You can use range() in your list comprehension to make i go from 0 to len(new_prices) - 1.
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print("Cuts under $30: ", cuts_under_30)

'''
Learn Python 3
Carly's Clippers
You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

You have been provided with three lists:

hairstyles: the names of the cuts offered at Carly’s Clippers.
prices: the price of each hairstyle in the hairstyles list.
last_week: the number of purchases for each hairstyle type in the last week.
Each index in hairstyles corresponds to an associated index in prices and last_week.

For example, The hairstyle "bouffant" has an associated price of 30 from the prices list, and was purchased 2 times in the last week as shown in the last_week list. Each of these elements are in the first index of their respective lists.

Let’s get started!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

Tasks
13/13 complete
Mark the tasks as complete by checking them off
Prices and Cuts:

Task 1
Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.

First, let’s sum up all the prices of haircuts. Create a variable total_price, and set it to 0.


Task 2
Loop through the prices list and add each price to the variable total_price.


Task 3
After your loop, create a variable called average_price that is the total_price divided by the number of prices.

You can get the number of prices by using the len() function.


Task 4
Print the value of average_price so the output looks like:

Average Haircut Price: <average_price>


Task 5
That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.

Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.


Task 6
Print new_prices.

Revenue:

Task 7
Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

Create a variable called total_revenue and set it to 0.


Task 8
Use a for loop to create a variable i that goes from 0 to len(hairstyles)

Hint: You can use range() to do this!


Task 9
Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.


Task 10
After your loop, print the value of total_revenue, so the output looks like:

Total Revenue: <total_revenue>


Task 11
Find the average daily revenue by dividing total_revenue by 7. Call this number average_daily_revenue and print it out.


Task 12
Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.

You can use range() in your list comprehension to make i go from 0 to len(new_prices) - 1.


Task 13
Print cuts_under_30.


'''