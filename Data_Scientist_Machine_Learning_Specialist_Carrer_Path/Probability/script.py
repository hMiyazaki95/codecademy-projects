'''
Catherine is going to visit the Inference and Machine Learning Teams this week. She knows that both of these specialists work with Probability, and wants to brush up on her skills before she goes, so she’s going to explore a famous problem – about birthdays.

Calculating the probability of an event is sometimes dependent on external factors. For instance, in the birthday problem “What is the probability that two people in a room have the same birthday?” the probability is dependent on the number of people in the room.

Other times, the probability of something is constant. For instance, the probability of flipping a coin and it landing heads will always be 50%.


In data science, probability is often used to simulate scenarios.

The code on the right simulates the birthday problem. Right now the code simulates a room with only 2 people that get random birthdays, and the probability that those 2 people have the same birthday is really low.

Change the number 2 to a higher number of your choosing where it says #Change This Number and run the code.

Is there a match in the simulation? What’s the probability that there would be a match?

Keep changing the number to test out different simulations.

Note that if you make your number too big, the program will throw an error due to the way we have implemented some of the math. This is a great example of needing to be mindful of possible inputs to your program!

'''




from simulate import simulate

num_people_in_room = 68 			#Change This Number (keep it smaller than 100 to save processing power)

simulate(num_people_in_room) 


'''

Here's what our room looks like:

Person 1's birthday: July 22
Person 2's birthday: October 16
Person 3's birthday: September 10
Person 4's birthday: March 20
Person 5's birthday: October 18
Person 6's birthday: July 18
Person 7's birthday: June 27
Person 8's birthday: February 18
Person 9's birthday: August 30
Person 10's birthday: January 10
Person 11's birthday: July 1
Person 12's birthday: September 2
Person 13's birthday: December 4
Person 14's birthday: July 26
Person 15's birthday: February 4
Person 16's birthday: February 3
Person 17's birthday: November 14
Person 18's birthday: January 31
Person 19's birthday: April 11
Person 20's birthday: July 17
Person 21's birthday: February 23
Person 22's birthday: March 20
Person 23's birthday: April 3
Person 24's birthday: February 23
Person 25's birthday: May 29
Person 26's birthday: February 10
Person 27's birthday: November 19
Person 28's birthday: November 12
Person 29's birthday: January 3
Person 30's birthday: August 1
Person 31's birthday: January 3
Person 32's birthday: August 29
Person 33's birthday: March 1
Person 34's birthday: March 1
Person 35's birthday: October 1
Person 36's birthday: September 23
Person 37's birthday: March 31
Person 38's birthday: July 25
Person 39's birthday: April 5
Person 40's birthday: April 14
Person 41's birthday: July 24
Person 42's birthday: March 1
Person 43's birthday: May 13
Person 44's birthday: October 23
Person 45's birthday: June 30
Person 46's birthday: September 15
Person 47's birthday: January 31
Person 48's birthday: October 24
Person 49's birthday: December 26
Person 50's birthday: November 18
Person 51's birthday: September 19
Person 52's birthday: April 6
Person 53's birthday: August 12
Person 54's birthday: July 4
Person 55's birthday: July 11
Person 56's birthday: August 28
Person 57's birthday: October 7
Person 58's birthday: May 29
Person 59's birthday: November 3
Person 60's birthday: December 16
Person 61's birthday: February 18
Person 62's birthday: March 8
Person 63's birthday: June 21
Person 64's birthday: October 11
Person 65's birthday: January 23
Person 66's birthday: May 20
Person 67's birthday: September 11
Person 68's birthday: April 5


The probability that two people in a room of 68 people have the same birthday is nearly 99.87%


In our simulation, the following people have the same birthdays: 
Person 22
Person 4
'''