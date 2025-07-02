import numpy as np
from scipy.stats import ttest_1samp
import pandas as pd
import matplotlib.pyplot as plt

# In this Project, we’ll walk through the implementation of a one-sample t-test in Python.
# One-sample t-tests are used for comparing a sample average to a hypothetical population average.
# For example, a one-sample t-test might be used to address questions such as:

# Is the average amount of time that visitors spend on a website different from 5 minutes?
# Is the average amount of money that customers spend on a purchase more than 10 USD?

# Suppose that a product manager wants online BuyPie orders to cost around 1000 Rupees on average.
# In the past day, 50 people made an online purchase and the average payment per order was less than 1000 Rupees.
# Are people really spending less than 1000 Rupees on average? Or is this the result of chance and a small sample size?

# Reading the prices:
prices = np.genfromtxt("prices.csv") # This reads as a list
print(prices[:10])

# Calculate mean
prices_mean = np.mean(prices)
print(f"The mean price is {prices_mean}.")
# 980, a little less than 1000.

# Suppose that we want to run a one-sample t-test with the following null and alternative hypotheses:
# Null: The average cost of a BuyPie order is 1000 Rupees
# Alternative: The average cost of a BuyPie order is not 1000 Rupees.
# SciPy has a function called ttest_1samp(), which performs a one-sample t-test for you.
# ttest_1samp() requires two inputs, a sample distribution and a mean to test against (eg. 1000):

stat, pval = ttest_1samp(prices, 1000)
print(f"The p-value is {pval :.3f}")
# This p-value is the probability of observing an average purchase price less than 980
# OR more than 1020 among a sample of 50 purchases.
# if p-value > 0.05, means it was a random chance, null hypothesis is correct
# if p-value < 0.05, means it was not a random, and we got with alternative hypothesis.

# Assumptions of a one-sample t-test include:
# The sample was randomly drawn from the population of interest
# The observations in the sample are independent
# The sample size is large “enough” or the sample data is normally distributed
# Plot your histogram here
plt.hist(prices)
plt.title("Sample mean for prices")
plt.xlabel("Cost")
plt.ylabel("Sample means")
plt.show()



