import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Reading data from the csv file
books = pd.read_csv("top-hundred-books.csv")

# Printing first four rows
#print(books.head())

# Reading in author ages
author_ages = books["Ages"]
#print(author_ages)

# Calculate the average, median and mode values of the author_ages array
ages_mean = np.average(author_ages)
ages_median = np.median(author_ages)
ages_mode = statistics.mode(author_ages)
print(f"The mean age for the authors is {ages_mean}.")
print(f"The median age for the authors is {ages_median}.")
print(f"The mode age for the authors is {ages_mode}.")

# Plotting a histogram to see where these values lie
plt.hist(author_ages, range = (10, 80), bins = 14)
plt.title("Publication Ages of Authors")
plt.xlabel("Ages")
plt.ylabel("Frequency")
plt.axvline(float(ages_median), color = "red", linestyle="dashed", linewidth = 3,label = "Median")
plt.axvline(float(ages_mean), color = "green", linestyle="dotted", linewidth = 3, label = "Mean")
plt.axvline(ages_mode, color = "blue", linestyle="solid", linewidth = 3, label = "Mode")
plt.legend()
plt.show()

#All three statistics are centered around the middle bars, close to each other.
