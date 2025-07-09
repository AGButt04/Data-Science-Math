import numpy as np
import scipy.stats as stats

# The variance of a binomial distribution is how much the expected value of success
# (from the previous exercise) may vary. In other words, it is a measurement of the spread
# of the probabilities to the mean/expected value.
# Variance for the Binomial distribution is similarly calculated to the expected value
# using the n (# of trials) and p (probability of success) parameters.
# Variance of expected value: n * p * (1 - p)

# A certain basketball player has an 85% chance of making a given free throw.
# What is the variance of free throws made from 20 shots.
variance_baskets = 20 * 0.85 * (1-0.85)
print(variance_baskets)

# Let’s say a student has a 98% chance of arriving on time to class.
# What is the variance of days the student will arrive late to class throughout the 180 school days in a school year.
variance_late = 180 * 0.98 * (1-0.98)
print(variance_late)

# At the end of the year, your company’s boss decides that the end-of-year bonus will be 8% of each employee’s salary.
# If the average salary in the company is $75,000, what is the expected value (or average value) of the bonuses?
bonus_expected = 75000 * 0.08
print(bonus_expected)

# Let’s say that the number of goals a soccer team scores follows the Poisson distribution with lambda equal to four.
# Calculate the variance of 100 random draws from games following this Poisson distribution.
num_goals = stats.poisson.rvs(4, size = 100)
print(num_goals)
print(np.var(num_goals))
# Counting each goal as 2
num_goals_2 = num_goals * 2
print(np.var(num_goals_2))

print("Exercise questions:")
# Let’s practice calculating different values from the Poisson distribution.
# Task - 1: You work at ambulance dispatch where the number of calls that come in daily follows the
# Poisson distribution with lambda equal to 9. There’s a rule that a team can go on no more than 12 calls a day.
# What is the probability of observing more than 12 calls on a given day.
calls = 1 - stats.poisson.cdf(12, 9)
print(calls)

# Task-2 : Let’s say that you have to call in a backup team if you have 10 or more calls in a given day.
# But you don’t want to have to call in a backup team unless they really will be needed.
# But what is the probability of observing a minimum of 10 calls, but no more than 12.
false_backup = stats.poisson.cdf(12, 9) - stats.poisson.cdf(9, 9)
print(false_backup)

# Task-3:  A certain tennis star has a first-serve rate of 62%. Let’s say they serve 80 times in a given match.
# What is the expected value of the number of serves they make?
serves = 80 * 0.68
print(serves)

# Task-4: At the same first-serve rate, what is the variance of this player’s first-serves?
serves_var = 80 * 0.68 * (1-0.68)
print(serves_var)