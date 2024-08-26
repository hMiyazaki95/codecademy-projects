# Sal's Shipping
# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

# In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

# Sal’s Shippers has several different options for a customer to ship their package:

# Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
# Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
# Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
# Here are the prices:

# Ground Shipping

# Weight of Package	Price per Pound	Flat Charge
# 2 lb or less	$1.50	$20.00
# Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
# Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
# Over 10 lb	$4.75	$20.00

# Ground Shipping Premium

# Flat charge: $125.00

# Drone Shipping

# Weight of Package	Price per Pound	Flat Charge
# 2 lb or less	$4.50	$0.00
# Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
# Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
# Over 10 lb	$14.25	$0.00

# Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

# Note that the walkthrough video for this project is slightly out of date — the walkthrough was done using a version of this project that uses functions. Feel free to come back to the video after having been introduced to functions!

# Tasks
# 7/9 complete
# Mark the tasks as complete by checking them off
# Ground Shipping:
# 1.
# First things first, define a weight variable and set it equal to any number.

# Stuck? Get a hint
# 2.
# Next, we need to know how much it costs to ship a package of given weight by normal ground shipping based on the “Ground shipping” table above.

# Write a comment that says “Ground Shipping”.

# Create an if/elif/else statement for the cost of ground shipping. It should check for weight, and print the cost of shipping a package of that weight.

# Stuck? Get a hint
# 3.
# A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:

# 8
# .
# 4
 
# 𝑙
# 𝑏
# ×
# $
# 4
# .
# 0
# 0
# +
# $
# 2
# 0
# .
# 0
# 0
# =
# $
# 5
# 3
# .
# 6
# 0
# 8.4 lb×$4.00+$20.00=$53.60
# Test that your ground shipping calculation gets the same value.

# Stuck? Get a hint
# Ground Shipping Premium:
# 4.
# We’ll also need to make sure we include the price of premium ground shipping in our code.

# Create a variable for the cost of premium ground shipping.

# Note: This does not need to be an if statement because the price of premium ground shipping does not change with the weight of the package.

# Stuck? Get a hint
# 5.
# Print it out for the user just in case they forgot!

# Stuck? Get a hint
# Drone Shipping:
# 6.
# Write a comment for this section of the code, “Drone Shipping”.

# Create an if/elif/else statement for the cost of drone shipping. This statement should check against weight and print the cost of shipping a package of that weight.

# Stuck? Get a hint
# 7.
# A package that weighs 1.5 pounds should cost $6.75 to ship by drone:

# 1
# .
# 5
 
# 𝑙
# 𝑏
# ×
# $
# 4
# .
# 5
# 0
# +
# $
# 0
# .
# 0
# 0
# =
# $
# 6
# .
# 7
# 5
# 1.5 lb×$4.50+$0.00=$6.75
# Test that your drone shipping calculation gets the same value.

# Solution:
# 8.
# Great job! Now, test everything one more time!

# What is the cheapest method of shipping a 4.8 pound package and how much would it cost?

# What is the cheapest method of shipping a 41.5 pound package and how much would it cost?

# (See hint for answers)

# Stuck? Get a hint
# 9.
# Don’t forget to check off all the tasks before moving on.

# Sample solutions:

# shipping.py
# P.S. If you make something cool, share it with us!
#shipping.py

#Types of shipping  
  #Ground Shipping
    #conditional statement 
# Weight of Package	      Price per Pound	  Flat Charge
# 2 lb or less	          $1.50	            $20.00
# Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
# Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
# Over 10 lb	$4.75	$20.00

  #Ground Shipping Premium
    #conditional statement
    # Flat charge: $125.00
  #Drone Shipping (new)
    #conditional statement
#     Weight of Package	Price per Pound	Flat Charge
# 2 lb or less	$4.50	$0.00
# Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
# Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
# Over 10 lb	$14.25	$0.00
  
# define a weight variable and assign it to any number you want to test
# weight = 8.4 # first test value
#weight = 1.5 # test value for drone
#weight = 4.8 # too check what is the cheapest method for shipping this weight.
weight = 41.5 # too check what is the cheapest method for shipping this weight.
Flat_Charges_Ground_Shipping = 20.00
Flat_Charges_Ground_Shipping_P = 125.00


# find each cost based on each pachage weight in noraml ground shipping

#Ground Shipping
if weight <= 2:
  price_per_pound = 1.50
elif weight > 2 and weight <= 6:
  price_per_pound = 3.00
elif weight > 6 and weight <= 10:
  price_per_pound = 4.00
else: #weight > 10
  price_per_pound = 4.75

cost_ground = weight * price_per_pound + Flat_Charges_Ground_Shipping
print('Cost of Ground Shipping: $' + str(cost_ground))

cost_ground_premium = weight * price_per_pound + Flat_Charges_Ground_Shipping_P
print('Cost of Ground Shipping Premium: $' + str(cost_ground_premium))


#Drone Shipping

if weight <= 2:
  price_per_pound_drone = 4.50
elif weight > 2 and weight <= 6:
  price_per_pound_drone = 9.00
elif weight > 6 and weight <= 10:
  price_per_pound_drone = 12.00
else: #weight > 10
  price_per_pound_drone = 14.25

cost_drone_shipping = weight * price_per_pound_drone
print("Cost of Drone Shipping: ${:.2f}".format(cost_drone_shipping))


# if weight == 1.5:
#   price_per_pound_drone = 6.75

# cost_drone_shipping = weight * price_per_pound_drone
# print("Cost of Drone Shipping: ${:.2f}".format(cost_drone_shipping))
