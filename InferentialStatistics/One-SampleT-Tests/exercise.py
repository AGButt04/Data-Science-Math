import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp

# As a final exercise, some data has been loaded with purchase prices for consecutive days at BuyPie.
# We can access the first day using daily_prices[0], the second using daily_prices[1], etc..
# Reading the daily_prices
daily_prices = np.genfromtxt("daily_prices.csv", delimiter=",")
print(daily_prices[0])

# Task-1: Calculate and print out a p-value for day 1 where the null hypothesis is that the average purchase price was 1000 Rupees
# and the alternative hypothesis is that the average purchase price was not 1000 Rupees. Print out the p-value
stat, pval = ttest_1samp(daily_prices[0], 1000)
print(f"The p-value for day 1: {pval :.3f}.")
# As the p-value > 0.05 (i.e. 0.607), we can't reject null hypothesis. It was a random chance.

# Task-10: Run the same hypothesis tests for days 1-10 and print out the resulting p-values.
# What’s the smallest p-value you observe for those 10 days?
p_values =[]
for i in range(10):
    day = daily_prices[i]
    stat, p_val = ttest_1samp(day, 1000.0)
    p_values.append(float(round(p_val,3)))
print(p_values)

# Try changing the null hypothesis so that the expected population mean that you’re testing against is different from 1000.
# Try any numbers that you want. How do your p-values change?
p_values =[]
for i in range(10):
    day = daily_prices[i]
    stat, p_val = ttest_1samp(day, 990)
    p_values.append(float(round(p_val,3)))
print(p_values)
# As you test values that are closer to the average of the data set, the p-values are getting smaller,
# stating alternative hypothesis is correct, and vice verse.

# Plotting to see if the sample is normally distributed
plt.hist(daily_prices[0])
plt.title("Sample mean for prices")
plt.xlabel("Cost")
plt.ylabel("Sample means")
plt.show()
