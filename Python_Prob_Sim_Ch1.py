import numpy as np

# Initialize seed and parameters
np.random.seed(123) 
lam, size_1, size_2 = 5, 3, 1000

# Draw samples & calculate absolute difference between lambda and sample mean

samples_1 = np.random.poisson(lam, size_1)
samples_2 = np.random.poisson(lam, size_2)
answer_1 = abs(lam - samples_1.mean())
answer_2 = abs(lam - samples_2.mean()) 

print("|Lambda - sample mean| with {} samples is {} and with {} samples is {}. ".format(size_1, answer_1, size_2, answer_2))

deck_of_cards=[('Diamond', 9),
 ('Spade', 9),
 ('Spade', 4),
 ('Club', 11),
 ('Club', 5),
 ('Heart', 11),
 ('Club', 8),
 ('Club', 0),
 ('Diamond', 4),
 ('Heart', 0),
 ('Heart', 5),
 ('Heart', 10),
 ('Spade', 10),
 ('Heart', 8),
 ('Heart', 12),
 ('Spade', 5),
 ('Spade', 11),
 ('Heart', 1),
 ('Heart', 6),
 ('Spade', 3),
 ('Diamond', 1),
 ('Spade', 0),
 ('Diamond', 5),
 ('Club', 2),
 ('Spade', 1),
 ('Diamond', 10),
 ('Heart', 7),
 ('Club', 7),
 ('Diamond', 11),
 ('Heart', 3),
 ('Club', 10),
 ('Diamond', 7),
 ('Heart', 4),
 ('Club', 3),
 ('Diamond', 8),
 ('Club', 1),
 ('Diamond', 12),
 ('Club', 12),
 ('Diamond', 0),
 ('Diamond', 2),
 ('Heart', 9),
 ('Spade', 6),
 ('Spade', 7),
 ('Club', 9),
 ('Diamond', 3),
 ('Club', 6),
 ('Club', 4),
 ('Spade', 12),
 ('Spade', 8),
 ('Spade', 2),
 ('Heart', 2),
 ('Diamond', 6)]
 
 
 # Shuffle the deck
np.random.shuffle(deck_of_cards) 

# Print out the top three cards
card_choices_after_shuffle = deck_of_cards[0:3]
print(card_choices_after_shuffle)



""" Throwing a fair die

Once you grasp the basics of designing a simulation, you can apply it to any system or process. Next, we will learn how each step is implemented using some basic examples.

As we have learned, simulation involves repeated random sampling. The first step then is to get one random sample. Once we have that, all we do is repeat the process multiple times. This exercise will focus on understanding how we get one random sample. We will study this in the context of throwing a fair six-sided die.

By the end of this exercise, you will be familiar with how to implement the first two steps of running a simulation - defining a random variable and assigning probabilities.

For the rest of the course, look to the IPython shell to find out what seed has been set. """




# Define die outcomes and probabilities
die, probabilities, throws = [1,2,3,4,5,6], [1/6, 1/6, 1/6, 1/6, 1/6, 1/6], 1

# Use np.random.choice to throw the die once and record the outcome
outcome = np.random.choice(die, size=throws, p=probabilities)
print("Outcome of the throw: {}".format(outcome[0]))


# Initialize number of dice, simulate & record outcome
die, probabilities, num_dice = [1,2,3,4,5,6], [1/6, 1/6, 1/6, 1/6, 1/6, 1/6], 2
outcomes = np.random.choice(die, size=num_dice, p=probabilities) 

# Win if the two dice show the same number
if outcomes[0] == outcomes[1]:
    answer = 'win' 
else: 
    answer = 'lose'

print("The dice show {} and {}. You {}!".format(outcomes[0], outcomes[1], answer))


""" Simulating the dice game

We now know how to implement the first three steps of a simulation. Now let's consider the next step - repeated random sampling.

Simulating an outcome once doesn't tell us much about how often we can expect to see that outcome. In the case of the dice game from the previous exercise, it's great that we won once. But suppose we want to see how many times we can expect to win if we played this game multiple times, we need to repeat the random sampling process many times. Repeating the process of random sampling is helpful to understand and visualize inherent uncertainty and deciding next steps.

Following this exercise, you will be familiar with implementing the fourth step of running a simulation - 

sampling repeatedly and generating outcomes. """





# Initialize model parameters & simulate dice throw
die, probabilities, num_dice = [1,2,3,4,5,6], [1/6, 1/6, 1/6, 1/6, 1/6, 1/6], 2
sims, wins = 100, 0

for i in range(sims):
    outcomes = np.random.choice(die, size=num_dice, p=probabilities) 
    # Increment `wins` by 1 if the dice show same number
    if outcomes[0] == outcomes[1]:
        wins = wins + 1

print("In {} games, you win {} times".format(sims, wins))



""" Simulating one lottery drawing

In the last three exercises of this chapter, we will be bringing together everything you've learned so far. We will run a complete simulation, take a decision based on our observed outcomes, and learn to modify inputs to the simulation model.

We will use simulations to figure out whether or not we want to buy a lottery ticket. Suppose you have the opportunity to buy a lottery ticket which gives you a shot at a grand prize of 1𝑀𝑖𝑙𝑙𝑖𝑜𝑛.𝑆𝑖𝑛𝑐𝑒𝑡ℎ𝑒𝑟𝑒𝑎𝑟𝑒1000𝑡𝑖𝑐𝑘𝑒𝑡𝑠𝑖𝑛𝑡𝑜𝑡𝑎𝑙,𝑦𝑜𝑢𝑟𝑝𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦𝑜𝑓𝑤𝑖𝑛𝑛𝑖𝑛𝑔𝑖𝑠1𝑖𝑛1000.𝐸𝑎𝑐ℎ𝑡𝑖𝑐𝑘𝑒𝑡𝑐𝑜𝑠𝑡𝑠
10. Let's use our understanding of basic simulations to first simulate one drawing of the lottery. """


# Pre-defined constant variables
lottery_ticket_cost, num_tickets, grand_prize = 10, 1000, 1000000

# Probability of winning
chance_of_winning = 1/num_tickets

# Simulate a single drawing of the lottery
gains = [-lottery_ticket_cost, grand_prize-lottery_ticket_cost]

probability = [1-chance_of_winning, chance_of_winning] 

outcome = np.random.choice(a=gains, size=1, p=probability, replace=True)

print("Outcome of one drawing of the lottery is {}".format(outcome))

""" Should we buy?

In the last exercise, we simulated the random drawing of the lottery ticket once. In this exercise, we complete the simulation process by repeating the process multiple times.

Repeating the process gives us multiple outcomes. We can think of this as multiple universes where the same lottery drawing occurred. We can then determine the average winnings across all these universes. If the average winnings are greater than what we pay for the ticket then it makes sense to buy it, otherwise, we might not want to buy the ticket.

This is typically how simulations are used for evaluating business investments. After completing this exercise, you will have the basic tools required to use simulations for decision-making.
"""


# Initialize size and simulate outcome
lottery_ticket_cost, num_tickets, grand_prize = 10, 1000, 1000000
chance_of_winning = 1/num_tickets
size = 2000
payoffs = [-lottery_ticket_cost, grand_prize-lottery_ticket_cost]
probs = [1-chance_of_winning, chance_of_winning]

outcomes = np.random.choice(a=payoffs, size=size, p=probs, replace=True)

# Mean of outcomes.
answer = outcomes.mean()
print("Average payoff from {} simulations = {}".format(size, answer))

""" Calculating a break-even lottery price

Simulations allow us to ask more nuanced questions that might not necessarily have an easy analytical solution. Rather than solving a complex mathematical formula, we directly get multiple sample outcomes. We can run experiments by modifying inputs and studying how those changes impact the system. For example, once we have a moderately reasonable model of global weather patterns, we could evaluate the impact of increased greenhouse gas emissions.

In the lottery example, we might want to know how expensive the ticket needs to be for it to not make sense to buy it. To understand this, we need to modify the ticket cost to see when the expected payoff is negative. """

# Initialize size and simulate outcome
lottery_ticket_cost, num_tickets, grand_prize = 10, 1000, 1000000
chance_of_winning = 1/num_tickets
size = 2000
payoffs = [-lottery_ticket_cost, grand_prize-lottery_ticket_cost]
probs = [1-chance_of_winning, chance_of_winning]

outcomes = np.random.choice(a=payoffs, size=size, p=probs, replace=True)

# Mean of outcomes.
answer = outcomes.mean()
print("Average payoff from {} simulations = {}".format(size, answer))

# Calculating a break-even lottery price

# Simulations allow us to ask more nuanced questions that might not necessarily have an easy analytical solution. Rather than solving a complex mathematical formula, we directly get multiple sample outcomes. We can run experiments by modifying inputs and studying how those changes impact the system. For example, once we have a moderately reasonable model of global weather patterns, we could evaluate the impact of increased greenhouse gas emissions.

# In the lottery example, we might want to know how expensive the ticket needs to be for it to not make sense to buy it. To understand this, we need to modify the ticket cost to see when the expected payoff is negative.



import matplotlib.pyplot as plt


plt.hist(outcomes)


""" Calculating a break-even lottery price

Simulations allow us to ask more nuanced questions that might not necessarily have an easy analytical solution. Rather than solving a complex mathematical formula, we directly get multiple sample outcomes. We can run experiments by modifying inputs and studying how those changes impact the system. For example, once we have a moderately reasonable model of global weather patterns, we could evaluate the impact of increased greenhouse gas emissions.

In the lottery example, we might want to know how expensive the ticket needs to be for it to not make sense to buy it. To understand this, we need to modify the ticket cost to see when the expected payoff is negative.
"""

# Initialize simulations and cost of ticket
sims, lottery_ticket_cost = 3000, 0

# Use a while loop to increment `lottery_ticket_cost` till average value of outcomes falls below zero
while 1:
    outcomes = np.random.choice([-lottery_ticket_cost, grand_prize-lottery_ticket_cost],
                 size=sims, p=[1-chance_of_winning, chance_of_winning], replace=True)
    if outcomes.mean() < 0:
        break
    else:
        lottery_ticket_cost += 1
        
        
answer = lottery_ticket_cost - 1

print("The highest price at which it makes sense to buy the ticket is {}".format(answer))







