import matplotlib.pyplot as plt
import numpy as np
from data import nba_data, okcupid_data

plt.hist(nba_data, alpha = 0.75, label = "NBA Data", bins = 20)
plt.hist(okcupid_data, alpha = 0.5, label = "OkCupid Data", bins = 20)
plt.xlabel("Height (inches)")
plt.legend()
plt.show()

nba_variance = np.var(nba_data)
cupid_variance = np.var(okcupid_data)
nba_mean = np.mean(nba_data)
cupid_mean = np.mean(okcupid_data)
print("The variance of the NBA dataset is " +str(nba_variance))
print("The variance of the OkCupid dataset is " +str(cupid_variance) + "\n")
print("The mean of the NBA dataset is " +str(nba_mean) + " inches")
print("The mean of the OkCupid dataset is " +str(cupid_mean) + " inches")

# Standard deviation is just square root of variance
nba_standard_deviation = nba_variance ** 0.5
cupid_standard_deviation = cupid_variance ** 0.5

print("The standard deviation of the NBA dataset is " +str(nba_standard_deviation))
print("The standard deviation of the OkCupid dataset is " + str(cupid_standard_deviation))

# Use NumPy's function!
nba_std = np.std(nba_data)
cupid_std = np.std(okcupid_data)

print("The standard Deviation using NumPy:")
print("The standard deviation of the NBA dataset is " +str(nba_std))
print("The standard deviation of the OkCupid dataset is " + str(cupid_std))

# Using standard deviation, let's see how many deviation away Lebron James is from either data_Set.
# In fact, you can usually expect around 68% of your data to fall within one standard deviation of the mean,
# 95% of your data to fall within two standard deviations of the mean, and 99.7% of your data to fall within
# three standard deviations of the mean.
# Lebron's height is 80 inches.

nba_diff = 80 - nba_mean
cupid_diff = 80 - cupid_mean

# Deviation is diff - std(dataset)
nba_dev = nba_diff / nba_std
cupid_dev = cupid_diff / cupid_std
print(f"\nYour basketball player is {nba_dev :.3f} standard deviations away from the mean of NBA player heights")
print(f"Your basketball player is {cupid_dev :.3f} standard deviations away from the mean of OkCupid profile heights")

# As lebron's height is almost 3 standard deviation away from ok-cupid data, means he is pretty unusual in that dating pool.

# Let's see where I stand in both of these data sets according to my height, using standard deviations.
# We can visually see using histogram.

my_height = 74

plt.subplot(211)
plt.title("NBA Player Heights")
plt.xlabel("Height (inches)")

plt.hist(nba_data)

plt.axvline(nba_mean, color='#FD4E40', linestyle='solid', linewidth=2, label = "Mean")
# plotting standard deviations
plt.axvline(nba_mean + nba_std, color='#FFB908', linestyle='solid', linewidth=2, label = "Standard Deviations")
plt.axvline(nba_mean - nba_std, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(nba_mean + nba_std * 2, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(nba_mean - nba_std * 2, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(nba_mean + nba_std * 3, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(nba_mean - nba_std * 3, color='#FFB908', linestyle='solid', linewidth=2)
# Plotting my height
plt.axvline(my_height, color='#62EDBF', linestyle='solid', linewidth=2, label = "Me")

plt.xlim(55, 90)
plt.legend()


plt.subplot(212)
plt.title("OkCupid Profile Heights")
plt.xlabel("Height (inches)")

plt.hist(okcupid_data)
plt.axvline(cupid_mean, color='#FD4E40', linestyle='solid', linewidth=2, label = "Mean")
# plotting standard deviations
plt.axvline(cupid_mean + cupid_std, color='#FFB908', linestyle='solid', linewidth=2, label = "Standard Deviations")
plt.axvline(cupid_mean - cupid_std, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(cupid_mean + cupid_std * 2, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(cupid_mean - cupid_std * 2, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(cupid_mean + cupid_std * 3, color='#FFB908', linestyle='solid', linewidth=2)
plt.axvline(cupid_mean - cupid_std * 3, color='#FFB908', linestyle='solid', linewidth=2)
# Plotting my height
plt.axvline(my_height, color='#62EDBF', linestyle='solid', linewidth=2, label = "You")

plt.xlim(55, 90)
plt.legend()
plt.tight_layout()
plt.show()

# I fall one standard deviation away from both data sets (positive
# for ok-cupid, and negative for NBA dataset