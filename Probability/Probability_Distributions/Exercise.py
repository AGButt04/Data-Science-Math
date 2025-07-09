import scipy.stats as stats
import numpy as np

# Task 1- sampling from a 6-sided die
lis = range(1,7)
sample = np.random.choice(lis, size = 4, replace = True)
print("ludo sample: " + str(sample))

## Task 2 - binomial probability mass function
# 6 heads from 10 fair coin flips
six = stats.binom.pmf(6, 10, 0.5)
print("The probability of getting exactly 6 heads out of 10 fair coin flips: " + str(six * 100) + "%")

# Task 3 - binomial probability mass function
# 2 to 4 heads from 10 coin flips
# P(X = 2) + P(X = 3) + P(X = 4)
two_four = stats.binom.pmf(2, 10, 0.5) + stats.binom.pmf(3, 10, 0.5) + stats.binom.pmf(4, 10, 0.5)
print("The probability of getting 2 to 4 heads: " + str(two_four * 100) + "%")
# 0 to 8 heads from 10 coin flips
# 1 - (P(X = 9) + P(X = 10))
eight_heads = 1 - (stats.binom.pmf(9, 10, 0.5) + stats.binom.pmf(10, 10, 0.5))
print("The probability of getting 0 to 8 heads: " + str(eight_heads * 100) + "%")

## Task 4 - binomial cumulative distribution function
# 6 or fewer heads from 10 coin flips
till_six = stats.binom.cdf(6, 10, 0.5)
print("The probability of six or fewer heads: " + str(till_six * 100) + "%")
# more than 6 heads from 10 coin flips
more_than6 = 1 - stats.binom.cdf(6, 10, 0.5)
print("The probability of more than 6 heads: " + str(more_than6) + "%")
# between 4 and 8 heads from 10 coin flips
four8 = stats.binom.cdf(8, 10, 0.5) - stats.binom.cdf(3, 10, 0.5)
print("The probability of getting 4 to 8 heads: " + str(four8 * 100) + "%")

## Task 5 - normal distribution cumulative distribution function
# stats.norm.cdf(x, loc, scale)
# temperature being less than 14*C
  # x = 14, loc = 20, scale = 3
temp = stats.norm.cdf(14, 20, 3)
print("The probability of getting 0-14 degrees celsius: " + str(temp * 100) + "%")

# Task 6
# temperature being greater than 24*C
  # x = 24, loc = 20, scale = 3
tempe = 1 - stats.norm.cdf(24, 20, 3)
print("The probability of getting temperature more than 24: " + str(tempe * 100) + "%")
# temperature being between 21*C and 25*C
  # x = 24, loc = 20, scale = 3
temperature = stats.norm.cdf(25, 20, 3) - stats.norm.cdf(21, 20, 3)
print("The probability of temperature between 21 and 25: " + str(temperature*100) + "%")