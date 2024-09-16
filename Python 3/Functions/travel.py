'''
Defining a Function

A function consists of many parts, so let’s first get familiar with its core - a function definition.

Here’s an example of a function definition:

def function_name():
  # functions tasks go here

There are some key components we want to note here:

The def keyword indicates the beginning of a function (also known as a function header). The function header is followed by a name in snake_case format that describes the task the function performs. It’s best practice to give your functions a descriptive yet concise name.

Following the function name is a pair of parenthesis ( ) that can hold input values known as parameters (more on parameters later in the lesson!). In this example function, we have no parameters.

A colon : to mark the end of the function header.

Lastly, we have one or more valid python statements that make up the function body (where we have our python comment).

Notice we’ve indented our # function tasks go here comment. Like loops and conditionals, code inside a function must be indented to show that they are part of the function.

Here is an example of a function that greets a user for our trip planning application:

def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")

Note: Pasting this code into the editor and clicking Run will result in an empty output terminal. The print() statements within the function will not execute since our function hasn’t been used. We will explore this further in the next exercise; for now, let’s practice defining a function.
'''
# Your code below: 
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")

directions_to_timesSq()

'''
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  print("Take lots of pictures!")

# Call your function here:

directions_to_timesSq()
'''




'''
Whitespace & Execution Flow

Consider our welcome function for our trip planning application:

def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")

The print statements all run together when trip_welcome() is called. This is because they have the same base level of indentation (2 spaces).

In Python, the amount of whitespace tells the computer what is part of a function and what is not part of that function.

If we wanted to write another statement outside of trip_welcome(), we would have to unindent the new line:

def trip_welcome():
  # Indented code is part of the function body
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")

# Unindented code below is not part of the function body
print("Woah, look at the weather outside! Don't walk, take the train!")

trip_welcome()

Our trip_welcome() function steps will not print Woah, look at the weather outside! Don't walk, take the train! on our function call. The print() statement was unindented to show it was not a part of the function body but rather a separate statement.

We would see the following output from this program:

Woah, look at the weather outside! Don't walk, take the train!
Welcome to Tripcademy!
Let's get you to your destination.

Lastly, note that the execution of a program always begins on the first line. The code is then executed one line at a time from top to bottom. This is known as execution flow and is the order a program in python executes code.

Woah, look at the weather outside! Don't walk, take the train! was printed before the print() statements from the function trip_welcome().

Even though our function was defined before our lone print() statement, we didn’t call our function until after.

Let’s play around with indentation and the flow of execution!

Instructions
Checkpoint 1 Passed
1.
We are going to help our trip planner users figure out if they should travel today based on the weather. Let’s let our users know we can check the weather for them.

Write a print() statement that will output Checking the weather for you!.

Stuck? Get extra guidance
Checkpoint 2 Passed
2.
We took a look outside and see a bright sunny day. Write a function called weather_check() that will print a message to our users that it’s a great day to travel! The function should output:

Looks great outside! Enjoy your trip.

Note: Don’t call your function just yet! We will do that in the next step.

Stuck? Get extra guidance
Checkpoint 3 Passed
3.
Oh no! It looks like some clouds came in and it started raining. Our users shouldn’t go on a trip in the rain. In our weather_check() function add a second print() statement under the first one which prints a warning message for our travelers! It should print:

False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.

Stuck? Get extra guidance
Checkpoint 4 Passed
4.
Call the function weather_check().

Stuck? Get extra guidance
Checkpoint 5 Passed
5.
Unindent the final print statement (the one starting with “False Alarm”) in your weather_check() function. Run the program again.

What is different?
'''
# Your code below: 
print("Checking the weather for you!")
def weather_check():
 print("Looks great outside! Enjoy your trip.")
print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")
weather_check()



'''
Parameters & Arguments

Let’s return to our trip_welcome() function one more time! Let’s modify our function to give a welcome that is a bit more detailed.

def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to Times Square today.")

trip_welcome()

This will output:

Welcome to Tripcademy!
Looks like you're going to Times Square today.

Our function does a really good job of welcoming anyone who is traveling to Times Square but a really poor job if they are going anywhere else. In order for us to make our function a bit more dynamic, we are going to use the concept of function parameters.

Function parameters allow our function to accept data as an input value. We list the parameters a function takes as input between the parentheses of a function ( ).

Here is a function that defines a single parameter:

def my_function(single_parameter)
  # some code

In the context of our trip_welcome() function, it would look like this:

def trip_welcome(destination):
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")

In the above example, we define a single parameter called destination and apply it in our function body in the second print statement. We are telling our function it should expect some data passed in for destination that it can apply to any statements in the function body.

But how do we actually use this parameter? Our parameter of destination is used by passing in an argument to the function when we call it.

trip_welcome("Times Square")

This would output:

Welcome to Tripcademy!
Looks like you're going to Times Square today. 

To summarize, here is a quick breakdown of the distinction between a parameter and an argument:

The parameter is the name defined in the parenthesis of the function and can be used in the function body.
A function definition in Python

The argument is the data that is passed in when we call the function, which is then assigned to the parameter name.
Calling a function with a specific value like trip_welcome("Empire State Building")

Let’s write a function with parameters and call the function with an argument to see it all in action!
'''

# Your code below:
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit", location)
  print("You can use the public subway system to get to", location)

generate_trip_instructions("Grand Central Station")



'''
Multiple Parameters
12 min
Using a single parameter is useful but functions let us use as many parameters as we want! That way, we can pass in more than one input to our functions.

We can write a function that takes in more than one parameter by using commas:

def my_function(parameter1, parameter2, parameter3):
  # Some code

When we call our function, we will need to provide arguments for each of the parameters we assigned in our function definition.

# Calling my_function
my_function(argument1, argument2)

For example take our trip application’s trip_welcome() function that has two parameters:

def trip_welcome(origin, destination):
  print("Welcome to Tripcademy")
  print("Looks like you are traveling from " + origin)
  print("And you are heading to " + destination)

Our two parameters in this function are origin and destination. In order to properly call our function, we need to pass argument values for both of them.

The ordering of your parameters is important as their position will map to the position of the arguments and will determine their assigned value in the function body (more on this in the next exercise!).

Our function call could look like:

trip_welcome("Prospect Park", "Atlantic Terminal")

In this call, the argument value of "Prospect Park" is assigned to be the origin parameter, and the argument value of"Atlantic Terminal" is assigned to the destination parameter.

The output would be:

Welcome to Tripcademy
Looks like you are traveling from Prospect Park
And you are heading to Atlantic Terminal

Let’s practice writing and calling a multiple parameter function!
'''

# Write your code below: 

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  # car_rental_total is product of car_rental_rate and trip_time
  car_rental_total = car_rental_rate * trip_time
  # 10 for discount
  hotel_total = hotel_rate * trip_time - 10
  # total
  trip_total = car_rental_total + hotel_total + plane_ticket_price

  print(trip_total)
  return trip_total

# Step 5: call your function
calculate_expenses(200, 100, 100, 5)





'''
Types of Arguments
19 min
In Python, there are 3 different types of arguments we can give a function.

Positional arguments: arguments that can be called by their position in the function definition.

Keyword arguments: arguments that can be called by their name.

Default arguments: arguments that are given default values.

Positional Arguments are arguments we have already been using! Their assignments depend on their positions in the function call. Let’s look at a function called calculate_taxi_price() that allows our users to see how much a taxi would cost to their destination 🚕.

def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )

In this function, miles_to_travel is positioned as the first parameter, rate is positioned as the second parameter, and discount is the third. When we call our function, the position of the arguments will be mapped to the positions defined in the function declaration.

# 100 is miles_to_travel
# 10 is rate
# 5 is discount
calculate_taxi_price(100, 10, 5)

Alternatively, we can use Keyword Arguments where we explicitly refer to what each argument is assigned to in the function call. Notice in the code example below that the arguments do not follow the same order as defined in the function declaration.

calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)

Lastly, sometimes we want to give our function parameters default values. We can provide a default value to a parameter by using the assignment operator (=). This will happen in the function declaration rather than the function call.

Here is an example where the discount argument in our calculate_taxi_price function will always have a default value of 10:

def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )

When using a default argument, we can either choose to call the function without providing a value for a discount (and thus our function will use the default value assigned) or overwrite the default argument by providing our own:

# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)

# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)

'''
# Write your code below:
def trip_planner(first_destination, second_destination,           
final_destination="Codecademy HQ"):
  #print("Here is what your trip will look like!")
  print("Here is what your trip will look like!", "First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")
trip_planner("Brooklyn", "Queens")


'''
Built-in Functions vs User Defined Functions
11 min
There are two distinct categories for functions in the world of Python. What we have been writing so far in our exercises are called User Defined Functions - functions that are written by users (like us!).

There is another category called Built-in functions - functions that come built into Python for us to use. Remember when we were using print or str? Both of these functions are built into the language for us, which means we have been using built-in functions all along!

There are lots of different built-in functions that we can use in our programs. Take a look at this example of using len() to get the length of a string:

destination_name = "Venkatanarasimharajuvaripeta"

# Built-in function: len()
length_of_destination = len(destination_name)

# Built-in function: print()
print(length_of_destination)

Would output the value of length_of_destination:

28

Here we are using a total of two built-in functions in our example: print(), and len().

And yes, if you’re wondering, that is a real railway station in India!

There are even more obscure ones like help() where Python will print a link to documentation for us and provide some details:

help("string")

Would output (shortened for readability):

NAME
    string - A collection of string constants.

MODULE REFERENCE
    https://docs.python.org/3.8/library/string
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.
.....

Check out all the latest built-in functions in the official Python docs.

Let’s practice using a few of them. You will need to rely on the provided Python documentation links to find your answers!
'''
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:

max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)

# round the price of the variable tshirt_price by one decimal place.
rounded_price = round(tshirt_price, 1)
print(rounded_price)



'''
Variable Access
7 min
As we expand our programs with more functions, we might start to ponder, where exactly do we have access to our variables? To examine this, let’s revisit a modified version of the first function we built out together:

def trip_welcome(destination):
  print(" Looks like you're going to the " + destination + " today. ")

What if we wanted to access the variable destination outside of the function? Could we use it? Take a second to think about what the following program will output, then check the result below!

def trip_welcome(destination):
  print(" Looks like you're going to the " + destination + " today. ")

print(destination)

Output Results

We call the part of a program where destination can be accessed its scope. The scope of destination is only inside the trip_welcome().

Take a look at another example:

budget = 1000

# Here we are using a default value for our parameter of `destination` 
def trip_welcome(destination="California"):
    print(" Looks like you're going to " + destination)
    print(" Your budget for this trip is " + str(budget))

print(budget)
trip_welcome()

Our output would be:

1000
Looks like you're going to California 
Your budget for this trip is 1000

Here we are able to access the budget both inside the trip_welcome function as well as our print() statement. If a variable lives outside of any function it can be accessed anywhere in the file.

We will be exploring the concept of scope more after this entire lesson but for now, let’s play around!

Note: Working with multiple functions can be a bit overwhelming at first. Don’t hesitate to use hints or even look at the solution code if you get stuck.
'''

# This function will print a hardcoded count of how many locations we have.
def print_count_locations():
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations(favorite_locations = "Paris, Norway, Iceland"):
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()


'''
Returns

At this point, our functions have been using print() to help us visualize the output in our interpreter. Functions can also return a value to the program so that this value can be modified or used later. We use the Python keyword return to do this.

Here’s an example of a program that will return a converted currency for a given location a user may want to visit in our trip planner application.

def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate

new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")

This would output:

100 dollars in US currency would give you 140 New Zealand dollars

Saving our values returned from a function like we did with new_zealand_exchange allows us to reuse the value (in the form of a variable) throughout the rest of the program.

When there is a result from a function that is stored in a variable, it is called a returned function value.

Let’s try to return some data in the exercises!

Note: Working with multiple functions can be a bit overwhelming at first. Don’t hesitate to use hints or even look at the solution code if you get stuck.
'''

current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

#print out the current budget by calling the function
print_remaining_budget(current_budget)

# Write your code below: 

def deduct_expense(budget, expense):
  return budget - expense

# shirt, cost 9 
shirt_expense = 9
# pass the two parameter to the new budget after shirt
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

# print remining budget
print_remaining_budget(new_budget_after_shirt)



'''
Multiple Returns
11 min
Sometimes we may want to return more than one value from a function. We can return several values by separating them with a comma. Take a look at this example of a function that allows users in our travel application to check the upcoming week’s weather (starting on Monday):

weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day

This function takes in a set of data in the form of a list for the upcoming week’s weather. We can get our returned function values by assigning them to variables when we call the function:

monday, tuesday, wednesday = threeday_weather_report(weather_data)

print(monday)
print(tuesday)
print(wednesday)

This will print:

Tomorrow the weather will be Sunny
The following day it will be Sunny
Two days from now it will be Cloudy

Let’s practice using multiple returns by returning to our previous code example.
'''

def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  # Add a line in the function top_tourist_locations_italy() that will return the values of first, second, third in that exact order.
  return first, second, third
#In order to use our three returned values from top_tourist_locations_italy() we need to assign them to new variables names after we call our function.
#Set the return of the function top_tourist_locations_italy() to be equal to three new variables called most_popular1, most_popular2, and most_popular3 in that exact order.

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)






'''

Review
Excellent work! 👏 In this lesson, you’ve covered a major fundamental programming concept used in the majority of all programs to organize code into reusable blocks. To recap, we explored:

What problems arise in our programs without functions
What functions are and how to write them
How whitespace plays an important role in how a program will execute our code and more importantly distinguish function code from non-function code
How to pass input values into our functions using parameters and arguments
The difference between built-in and user-defined functions and some common built-in functions python offers
How we can reuse function output with the return keyword, as well as multiple returns.
Where variables can be accessed in our programs that use functions
Let’s practice putting all these concepts together!

'''

def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0", name)

# input for parameter
trip_planner_welcome("Hajime Miyazaki")

#Define the function estimated_time_rounded() with a single parameter estimated_time
def estimated_time_rounded(estimated_time):
  # Create a variable called rounded_time that is the result of calling the round() built-in function on the parameter estimated_time
  rounded_time = round(estimated_time)
  # Return rounded_time
  return rounded_time
# After the function definition, call estimated_time_rounded() with a decimal argument and save the result to a variable called estimate. Since this amount represents a time, be sure to use a positive number.
estimate = estimated_time_rounded(.5)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in", origin)
  print("And you are traveling to", destination)
  print("You will be traveling by", mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")
  
destination_setup("San Francisco", "Las Vegas", 2, "Plane") 