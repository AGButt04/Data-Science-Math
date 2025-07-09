import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# The Poisson distribution is another common distribution, and it is used to describe the
# number of times a certain event occurs within a fixed time or space interval.
# For example, the Poisson distribution can be used to describe the number of cars that
# pass through a specific intersection between 4pm and 5pm on a given day. It can also be used to
# describe the number of calls received in an office between 1pm to 3pm on a certain day.

# Suppose we are working in a call center, and we expect the average number of calls in our call center
# between 9am and 10am to be 15 calls. What is the probability that we would see exactly 12 calls in that time frame?
prob_12 = stats.poisson.pmf(12, 15)
print(prob_12)

# What is the probability we would get between 7 and 9 calls?
prob_7_to_9 = stats.poisson.pmf(7, 15) + stats.poisson.pmf(8, 15) + stats.poisson.pmf(9, 15)
print(prob_7_to_9)

# Calculating Probabilities of a Range using the Cumulative Distribution Function
# What is the probability of observing more than 20 calls?
prob_20 = 1 - stats.poisson.cdf(20, 15)
print(prob_20)
# What is the probability of observing between 17 to 21 calls when the expected number of calls is 15?
prob_17_to_21 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)
print(prob_17_to_21)

# Expected value of Poisson Distribution
def histogram_function(randvars):
  plt.hist(rand_vars, bins = np.arange(len(set(randvars)))-0.5, edgecolor = "black")
  plt.xticks(list(range(rand_vars.max())))
  plt.show()

# Checkpoint 1
# lambda = 15, 1000 random draws
rand_vars = stats.poisson.rvs(15, size = 1000)
## Checkpoint 2
# print the mean of rand_vars
print(rand_vars.mean())
## Checkpoint 3
histogram_function(rand_vars)

# Probability distributions also have calculable variances. Variances are a way of measuring
# the spread or dispersion of values and probabilities in the distribution. For the Poisson distribution,
# the variance is simply the value of lambda (λ), meaning that the expected value and variance are equivalent in Poisson distributions.
# 5000 draws, lambda = 7
rand_vars_7 = stats.poisson.rvs(7, size = 5000)
# print variance of rand_vars_7
print(np.var(rand_vars_7))
# print minimum and maximum of rand_vars_7
print(min(rand_vars_7))
print(max(rand_vars_7))

# 5000 draws, lambda = 17
rand_vars_17 = stats.poisson.rvs(17, size = 5000)
# print variance of rand_vars_17
print(np.var(rand_vars_17))
# print minimum and maximum of rand_vars_17
print(min(rand_vars_17))
print(max(rand_vars_17))
# As we can see, as the parameter lambda increases,
# the variance — or spread — of possible values increases as well.