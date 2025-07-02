import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binomtest

# Binomial tests are useful for comparing the frequency of some outcome in a sample to the expected probability
# of that outcome. For example, if we expect 90% of ticketed passengers to show up for their flight but only 80 of 100
# ticketed passengers actually show up, we could use a binomial test to understand whether 80 is significantly different from 90.

# Binomial tests are similar to one-sample t-tests in that they test a sample statistic against some population-level expectation.
# The difference is that:
# binomial tests are used for binary categorical data to compare a sample frequency to an expected population-level probability.
# one-sample t-tests are used for quantitative data to compare a sample mean to an expected population mean.

# Reading the data from live-it-LIVE.com:
monthly_report = pd.read_csv('monthly_report.csv')
print(monthly_report.head())

# In order to run a hypothesis test to address this, we’ll first need to know two things from the data:
# The number of people who visited the website.
# The number of people who made a purchase on the website.
sample_size = len(monthly_report["purchase"])
purchased_prop = np.mean(monthly_report["purchase"] == 'y')
purchased_num = np.sum(monthly_report["purchase"] == 'y')
print("The number of people visited the site:" , sample_size)
print("The proportion of purchases items:", purchased_prop)
print("The number of purchased items:", purchased_num)

# We calculated that there were 500 site visitors to live-it-LIVE.com this month
# and 41 of them made a purchase. In comparison, if each of the 500 visitors had a 10% chance of making a purchase,
# we would expect around 50 of those visitors to buy something. Is 41 different enough from 50 that we should question
# whether this months’ site visitors really had a 10% chance of making a purchase?

# This is like flipping a coin whether heads or tails, probability for both is 0.5
# Let's flip 10 times.
coin_flips = np.random.choice(['Heads', 'Tails'], size = 10, p = [0.5, 0.5])
print(coin_flips)
# Simulate one visitor:
one_visitor = np.random.choice(['y', 'n'], size = 5, p = [0.1, 0.9])
print(one_visitor)
# Simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y', 'n'], size = 500, p = [0.1, 0.9])
# print(simulated_monthly_visitors)
count = sum(x == 'y' for x in simulated_monthly_visitors)
print("Number of people who made purchase in this simulated example:", count)
# It's around 50. It varies from sample to sample.

# Let's find the range:
# We can simulate the sample 10,000 and count the number of purchases of each sample.
# Find the min and max of that, it won't be perfect but it will give us some idea.
null_outcomes = []
for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size = 500, p = [0.1, 0.9])
    num_purchases = np.sum(simulated_monthly_visitors == "y")
    null_outcomes.append(num_purchases)

null_min = min(null_outcomes)
null_max = max(null_outcomes)
print("The minimum of the sample:", null_min)
print("The maximum of the sample:", null_max)
print("The difference between the minimum and maximum of the samples:", null_max - null_min)
# The range is (25, 75), The difference is around the expected mean.

# Inspecting the null distribution:
# In the month we’re investigating, we calculated that there were 41 purchases. Add a vertical line to the histogram at 41.
# Plot the histogram here:
plt.hist(null_outcomes)
plt.axvline(41, color = 'r')
plt.show()
# 41 purchases is somewhat likely to occur based on this null distribution.
# It’s not in the middle of the distribution, where there’s the most density,
# but it’s also not way out in the tails (which would mean it is very unlikely).

# Calculate an interval covering the middle 90% of the values in null_outcomes.
# By reporting an interval covering 95% of the values instead of the full range,
# we can say something like: “we are 95% confident that, if each visitor has a 10% chance of making a purchase,
# a random sample of 500 visitors will make between 37 and 63 purchases.
null_ninety = np.percentile(null_outcomes,[2.5, 97.5])
print("The ninety percent of the purchases: ", null_ninety)

# Use null_outcomes to estimate the p-value for a binomial hypothesis test with the following null and alternative hypotheses:
# Null: the probability of a purchase was 10%
# Alternative: the probability of a purchase rate was LESS THAN 10%

null_outcomes = np.array(null_outcomes)
less41 = np.sum(null_outcomes <= 41)
p_val_1_sided = less41 / len(null_outcomes)
print("The one sided p-value is ", p_val_1_sided)

# Use null_outcomes to calculate the p-value for a two-sided test
# (alternative hypothesis is that the purchase probability was DIFFERENT FROM 10%).
# In other words, calculate the proportion of values in null_outcomes that are less than or
# equal to 41 (the number of purchases we observed in our sample, which is 9 fewer than 50)
# OR greater than or equal to 59 (which is 9 purchases more than 50).

sums = np.sum((null_outcomes <= 41) | (null_outcomes >= 59))
p_val_2_sided = sums / len(null_outcomes)
print("The two_sided p-value is ", p_val_2_sided)
# The 2 sided p-value is double the 1-sided-p-value

# SciPy has a binominal test function which takes following arguments:
# The observed sample statistic (eg., 41 purchases)
# The sample size (e.g., 500 visitors)
# The null probability of success (eg., 0.10 probability of a purchase)
# calculate p_value_1sided here:
print("The p-values using SciPy's binom_test: ")
p_value2 = binomtest(41, 500, .1, alternative = 'less')
print("Binom_test 1 sided p-value: ", round(p_value2.pvalue, 3))
# It should be equal to p_val_1_sided.

# Calculate p_value_2sided here:
p_value_2sided = binomtest(41, n = 500, p = 0.10)
print("Binom_test 2 sided p-value: ", round(p_value_2sided.pvalue, 3))

