import numpy as np
import scipy.stats as stats

# You are in charge of monitoring the number of defective products from a specific factory.
# You’ve been told that the number of defects on a given day follows the Poisson distribution with the
# rate parameter (lambda) equal to 7. You’re new here, so you want to get a feel for what it means to
# follow the Poisson(7) distribution. So in this case, the expected value of
# the Poisson(7) distribution is 7 defects per day.
# You will investigate certain attributes of the Poisson(7) distribution to get an intuition for how many
# defective objects you should expect to see in a given amount of time.

### Task Group 1 ###
## Task 1:
lam = 7

## Task 2:
#Calculate and print the probability of observing exactly lam defects on a given day.
lam_def = stats.poisson.pmf(lam, lam)
print("The probability of lamda defects: " + str(lam_def * 100))

## Task 3:
# Having 4 or fewer defects on a given day is an exceptionally good day. Calculate and print the probability of having one of these days.
good_days = stats.poisson.cdf(4, lam)
print("The probability of good days: " + str(good_days * 100))

## Task 4:
# On the other hand, our boss said that having more than 9 defects on any given day is considered a bad day.Calculate and print the probability of having one of these bad days.
bad_days = 1 - stats.poisson.cdf(9, lam)
print("The probability of bad days: " + str(bad_days * 100))

### Task Group 2 ###
print("--Distribution in Practice--")

## Task 5:
# Create a variable called year_defects that has 365 random values from the Poisson distribution.
year_defects = stats.poisson.rvs(lam, size = 365)

## Task 6:
#Print first 20 values
print(year_defects[0 : 20])

## Task 7:
#If we expect 7 defects on a given day, what is the total number of defects we would expect over 365 days?Calculate and print this value to the output terminal.
total_defects = 365 * lam
print("Total defects: " + str(total_defects))

## Task 8:
# Calculate and print the total sum of the data set year_defects. How does this compare to the total number of defects we expected over 365 days?
total_sum = np.sum(year_defects)
print("Total sum: " + str(total_sum))
#It's really close to what we expected

## Task 9:
# Calculate and print the average number of defects per day from our simulated dataset.
average = np.mean(year_defects)
print("Average number of defects: " + str(average))
#It's close to our expected value (7) but not quite there.

## Task 10:
maxV = max(year_defects)
print("The maximum defects of the year: " + str(maxV))

## Task 11:
#Calculate and print the probability of observing that maximum value or more from the Poisson(7) distribution
max_value = 1 - stats.poisson.cdf(maxV, lam)
print("The probability of max defect or more: " + str(max_value))

### Extra Bonus ###
# Task 12
#Use this method (stats.poisson.ppf(percentile, lambda) to calculate and print the number of defects that would put us in the 90th percentile for a given day. In other words, on 90% of days, we will observe fewer defects than this number.
ninety = stats.poisson.ppf(0.9, lam)
print("The number of defects on 90% of days: " + str(ninety))

# Task 13
# Now let’s see what proportion of our simulated dataset year_defects is greater than or equal to the number we calculated in the previous step.
year_defects = np.array(year_defects)
num = np.sum((year_defects >= ninety))
proportion = num / len(year_defects)
print("The proportion of year defects: " + str(proportion * 100) + "%")