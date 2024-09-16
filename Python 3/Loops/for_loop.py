
# For Loops: Introduction

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

# Indent (2 spaces or tab) line 6 so that we don’t get an IndentationError when you run the code.
for game in board_games:
  print(game) # need indentation

# Write a for loop that prints each sport in the list sport_games.
for game in sport_games:
  print(game)



# For Loops: Using Range
promise = "I will finish the python loops module!"

# Use the range() function in a for loop to print() out the provided promise variable five times.
for temp in range(5): # 5 times -> index 0-4
    print(promise)