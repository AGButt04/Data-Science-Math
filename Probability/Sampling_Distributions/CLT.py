import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

# The Central Limit Theorem (CLT) allows us to specifically describe the sampling distribution of the mean.
# The CLT states that the sampling distribution of the mean is normally distributed as long as the population
# is not too skewed or the sample size is large enough. Using a sample size of n > 30 is usually a good rule of thumb,
# regardless of what the distribution of the population is like. If the distribution of the population is normal,
# the sample size can be smaller than that. The CLT not only establishes that the sampling distribution will be normally
# distributed, but it also allows us to describe that normal distribution quantitatively. Normal distributions are described
# by their mean μ (mu) and standard deviation σ (sigma).

# Set the population mean & standard deviation:
population_mean = 10
population_std_dev = 10
# Set the sample size:
samp_size = 6
# Create the population
population = np.random.normal(population_mean, population_std_dev, size = 100000)

# Simulate the samples and calculate the sampling distribution
sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)

# Plot the original population
sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} ")
plt.xlabel("")
plt.show()
plt.clf()

## Plot the sampling distribution
sns.histplot(sample_means, stat='density')
# calculate the mean and SE for the probability distribution
mu = np.mean(population)
sigma = np.std(population)/(samp_size**.5)
# plot the normal distribution with mu=popmean, sd=sd(pop)/sqrt(samp_size) on top
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

plt.plot(x, stats.norm.pdf(x, mu, sigma), color='k', label = 'normal PDF')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution}")
plt.xlabel("")
plt.show()

# Yes, what we are seeing aligns with the CLT. The sampling distribution of the mean looks like a
# bell curve and has a mean close to the population mean. Because the original population is normally distributed,
# the CLT applies even with a smaller sample size.