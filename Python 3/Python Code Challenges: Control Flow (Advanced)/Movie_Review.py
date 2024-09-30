'''
4. Movie Review
We want to create a function that will help us rate movies. Our function will split the ratings into different ranges and tell the user how the movie was based on the movie’s rating. Here are the steps needed:

Define our function to accept a single number called rating
If the rating is equal to or less than 5, return "Avoid at all costs!"
If the rating was less than 9, return "This one was fun."
If neither of the if statement conditions were met, return "Outstanding!"

Create a function named movie_review() that has one parameter named rating.

If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"
'''


def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating > 5 and rating < 9:
        return "This one was fun."
    elif rating >= 9:
        return "Outstanding!"
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."
    