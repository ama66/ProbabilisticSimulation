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






