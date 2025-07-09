import numpy as np
import scipy.stats as stats

# In this practice, we will use random.choice(a, size = size, replace = True/False)
# In this method:
# a is a list or other object that has values we are sampling from
# size is a number that represents how many values to choose
# replace can be equal to True or False, and determines whether we keep a value in a after drawing it
# (replace = True) or remove it from the pool (replace = False).

# Create a 6 sided die
die_6 = range(1, 7)
# set number of rolls
num_rolls = 10
# roll the "die" the set amount of times
results_1 = np.random.choice(die_6, size = num_rolls, replace = True)
print(results_1)

# A probability mass function (PMF) is a type of probability distribution that defines the probability of
# observing a particular value of a discrete random variable. For example, a PMF can be used to calculate the
# probability of rolling a three on a fair six-sided die.
# The binom.pmf() method from the scipy.stats library can be used to calculate the PMF of the
# binomial distribution at any value. This method takes 3 values:
# x: the value of interest
# n: the number of trials
# p: the probability of success
x = 7
n = 20
prob_1 = stats.binom.pmf(x, n, 0.5)
print(prob_1 * 100) #7 heads out of 20 coin flips
# Probability of observing between 4 to 6 heads from 10 coin flips.
prob_1 = stats.binom.pmf(4, 10, 0.5) + stats.binom.pmf(5, 10, 0.5) + stats.binom.pmf(6, 10, 0.5)
print(prob_1 * 100)
# Probability of observing more than 2 heads from 10 coin flips.
prob_2 = 1 - (stats.binom.pmf(0, 10, 0.5) + stats.binom.pmf(1, 10, 0.5) + stats.binom.pmf(2, 10, 0.5))
print(prob_2 * 100)

# The cumulative distribution function for a discrete random variable can be derived from the probability mass function.
# However, instead of the probability of observing a specific value, the cumulative distribution function gives the probability
# of observing a specific value OR LESS.
# We can use the binom.cdf() method to calculate the cumulative distribution function.
# This method takes 3 values:
# x: the value of interest, looking for the probability of this value or less
# n: the sample size
# p: the probability of success
##
prob_1 = stats.binom.cdf(3, 10, 0.5)
print(prob_1)

# compare to cdf code
print(stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) +
      stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5))

# Probability of observing more than 5 heads out of 10 coin flips.
prob_2 = 1 - stats.binom.cdf(5, 10, 0.5)
print(prob_2)

# Probability of observing between 2 and 5 heads from 10 fair coin flips.
prob_3 = stats.binom.cdf(5, 10,0.5) - stats.binom.cdf(1, 10, 0.5)
print(prob_3)
# Compare to cdf code
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) +
      stats.binom.pmf(4, n=10, p=.5) + stats.binom.pmf(5, n=10, p=.5))

# Let’s say we want to know the probability that a randomly chosen woman is less than 158 cm tall.
# We can use the cumulative distribution function to calculate the area under the probability density function
# curve from 0 to 158 to find that probability.
# When graphed, a probability density function is a curve across all possible values the random variable can take on,
# and the total area under this curve adds up to 1.
# We can calculate the area of the shaded region in Python using the norm.cdf() function.
# This method takes on 3 values:
# x: the value of interest
# loc: the mean of the probability distribution
# scale: the standard deviation of the probability distribution
prob = stats.norm.cdf(158, 167.64, 8)
print(prob)

# The probability that the weather on a randomly selected day will be between 18 to 25 degrees.
temp_prob_1 = stats.norm.cdf(25, 20, 3) - stats.norm.cdf(18, 20, 3)
print("The temp between 18 and 25: " + str(temp_prob_1))
# The probability that the weather on a randomly selected day will be greater than 24 degrees.
temp_prob_2 = 1 - stats.norm.cdf(24, 20, 3)
print("The temp greater than 24: " + str(temp_prob_2))
