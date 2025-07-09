import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# In statistics, we often want to learn about a large population. Since collecting data for an
# entire population is often impossible, researchers may use a smaller sample of data to try to answer their questions.
# To do this, a researcher might calculate a statistic such as mean or median for a sample of data.
# Then they can use that statistic as an estimate for the population value they really care about.

# The numpy.random package has several functions that we could use to simulate random sampling.
# In this exercise, we’ll use the function np.random.choice(), which generates a sample of some size from a given array.
pop = pd.read_csv("salmon_population.csv")
pop = np.array(pop["Salmon_Weight"])
pop_mean = round(np.mean(pop),3)

## Plotting the Population Distribution
sns.histplot(pop, stat='density')
plt.axvline(pop_mean,color='r',linestyle='dashed')
plt.title(f"Population Mean: {pop_mean}")
plt.xlabel("Weight (lbs)")
plt.show()
plt.clf() # close this plot
# Generate our random sample below
samp_size = 50
sample = np.random.choice(np.array(pop), samp_size, replace = False)
### Define sample mean below
sample_mean = round(np.mean(sample), 3)

### Uncomment the lines below to plot the sample data:
sns.histplot(sample, stat='density')
plt.axvline(sample_mean,color='r',linestyle='dashed')
plt.title(F"Sample Mean: {sample_mean}")
plt.xlabel("Weight (lbs)")
plt.show()
# Smaller sample sizes will have sample means that vary more from each other each time you take a random sample.
# With a small sample, extreme values can significantly impact the sample mean, causing it to vary from one sample to the next.

# As we saw in the last example, each time we sample from a population,
# we will get a slightly different sample mean. In order to understand how much variation
# we can expect in those sample means, we can do the following:
# Take a bunch of random samples of fish, each of the same size (50 fish in this example)
# Calculate the sample mean for each one
# Plot a histogram of all the sample means
# This process gives us an estimate of the sampling distribution of the mean for a sample size of 50 fish

population = pd.read_csv("cod_population.csv")
# Save transaction times to a separate numpy array
population = population['Cod_Weight']

sample_size = 50
sample_means = []
for i in range(500):
  samp = np.random.choice(population, sample_size, replace = False)
  # calculate mean here
  this_sample_mean = np.mean(samp)
  # append here
  sample_means.append(this_sample_mean)

sns.histplot(sample_means,stat='density')
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
plt.show()

# The tail of the population distribution is quite long on the right, so we can describe it as right-skewed.
# However, the sampling distribution seems normally distributed. You might be wondering why the sampling
# distribution is not right-skewed like the population distribution. That is because of Central Limit Theorem.
