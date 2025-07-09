import scipy.stats as stats

# The standard deviation of a sampling distribution is also known as the STANDARD ERROR of
# the estimate of the mean. In many instances, we cannot know the population standard deviation,
# so we estimate the standard error using the sample standard deviation:
# Sample Standard Deviation/(sample_size)**0.5
# Two important things to note about this formula is that:
# As sample size increases, the standard error will decrease.
# As the population standard deviation increases, so will the standard error.

# Let’s say we are transporting the salmon and want to make sure the crate we carry the fish in will be
# strong enough to hold the weight.
# Suppose we estimate that the salmon population has an average weight of 60 lbs with a standard deviation of 40 lbs.
# We have a crate that supports 750 lbs, and we want to be able to transport 10 fish at a time.
# We want to calculate the probability that the average weight of those 10 fish is less than or equal to 75 (750/10).
# Using the CLT, we first estimate that the mean weight of 10 randomly sampled salmon from this population is
# normally distributed with mean = 60 and standard error = 40/10^.5. Then, we can use this probability distribution
# to calculate the probability that 10 randomly sampled fish will have a mean weight less than or equal to 75.
x = 75
mean = 60
std_dev = 40
samp_size = 10
standard_error = std_dev / (samp_size**.5)
# remember that **.5 is raising to the power of one half, or taking the square root
prob_salmon = stats.norm.cdf(x,mean,standard_error)

# Let’s calculate the same probability for our cod fish population.
# We know that cod have an average weight of 36 lbs with a standard deviation of 20.
# We want to try to fit 25 cod fish into our same crate that can hold up to 750 lbs.
x = 750 / 25
mean = 36
std_dev = 20
samp_size = 25
std_err = std_dev / (samp_size**.5)
prob_cod = stats.norm.cdf(x,mean,std_err)
print(prob_cod)

