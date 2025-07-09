from helper_functions import (population_distribution, sampling_distribution)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# task 1: load in the spotify dataset
spotify_data = pd.read_csv("spotify_data.csv")

# task 2: preview the dataset
print(spotify_data.head())

# task 3: select the relevant column
song_tempos = spotify_data["tempo"]

# task 5: plot the population distribution with the mean labeled
population_distribution(song_tempos)

# task 6: sampling distribution of the sample mean
sampling_distribution(song_tempos, 30, "Mean")
# task 7: It's an unbiased estimator mean of the population.

# task 8: sampling distribution of the sample minimum
sampling_distribution(song_tempos, 30, "Minimum")
# task 9: The sample minimum is biased estimator of the population mean of minimums.

# task 10: sampling distribution of the sample variance
sampling_distribution(song_tempos, 30, "Variance")
# task 11: Mean variance appears to be an unbiased estimator as it is really close to the population mean

# task 12: It still is really close to the mean of the population variance, appears unbiased estimator

# task 13: calculate the population mean and standard deviation
population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)

# task 14: calculate the standard error
standard_error = population_std/ (30 ** 0.5)

# task 15: calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs
prop_140 = stats.norm.cdf(140, population_mean, standard_error)
print("The probability of song less than 140 bpm: " + str(prop_140 * 100) + "%")

# task 16: calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs
prop_150 = 1 - stats.norm.cdf(150, population_mean, standard_error)
print("The probability of songs greater than 150 bpm: " + str(prop_150 * 100) + "%")

# EXTRA
# What is the probability of getting a sample minimum that is less than 90 bpm?
sample_min = sampling_distribution(song_tempos, 30, "Minimum")
less_90 = sum(m < 90 for m in sample_min) / len(sample_min)
print("The probability of sample minimum less than 90: " + str(less_90 * 100) + "%")


