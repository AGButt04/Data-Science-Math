import statistics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

# Reading in housing data
brooklyn_one_bed = pd.read_csv("brooklyn-one-bed.csv")
brooklyn_price = brooklyn_one_bed["rent"]

queens_one_bed = pd.read_csv("queens-one-bed.csv")
queens_price = queens_one_bed["rent"]

manhattan_one_bed = pd.read_csv("manhattan-one-bed.csv")
manhattan_price = manhattan_one_bed["rent"]

# We can retrieve information about specific apartment as well (Complete Row).
# Most expensive apartments of each borough.
brooklyn_max = max(brooklyn_price)
most_expensive_B = brooklyn_one_bed[brooklyn_one_bed["rent"] == brooklyn_max]
size_B = most_expensive_B["size_sqft"].values[0]
print(f"Most expensive Apartment of Brooklyn is ${brooklyn_max} with {size_B} square feet.")

man_max = max(manhattan_price)
most_expensive_M = manhattan_one_bed[manhattan_one_bed["rent"] == man_max]
size_M = most_expensive_M["size_sqft"].values[0]
print(f"Most expensive Apartment of Manhattan is ${man_max} with {size_M} square feet.")

queen_max = max(queens_price)
most_expensive_Q = queens_one_bed[queens_one_bed["rent"] == queen_max]
size_Q = most_expensive_Q["size_sqft"].values[0]
print(f"Most expensive Apartment of Queens is ${queen_max}. with {size_Q} square feet")


# Add mean calculations below
brooklyn_mean = np.mean(brooklyn_price)
manhattan_mean = np.mean(manhattan_price)
queens_mean = np.mean(queens_price)

# Add median calculations below
brooklyn_median = np.median(brooklyn_price)
manhattan_median = np.median(manhattan_price)
queens_median = np.median(queens_price)

# Add mode calculations below
brooklyn_mode = stats.mode(brooklyn_price)
manhattan_mode = stats.mode(manhattan_price)
queens_mode = stats.mode(queens_price)

# # Plotting a histogram for each borough apartment prices
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))  # 3 rows, 1 column
fig.subplots_adjust(hspace=0.6)  # adds vertical spacing between subplots

# --- Brooklyn ---
ax1.hist(brooklyn_price, range=(0, 10000), bins=14)
ax1.set_title("Brooklyn Apartments Prices")
ax1.set_xlabel("Cost")
ax1.set_ylabel("Number of Apartments")
ax1.axvline(float(brooklyn_median), color="red", linestyle="dashed", linewidth=3, label="Median")
ax1.axvline(float(brooklyn_mean), color="black", linestyle="dotted", linewidth=3, label="Mean")
ax1.axvline(statistics.mode(brooklyn_price), color="orange", linestyle="solid", linewidth=3, label="Mode")
ax1.legend()

# --- Manhattan ---
ax2.hist(manhattan_price, range=(0, 10000), bins=14)
ax2.set_title("Manhattan Apartments Prices")
ax2.set_xlabel("Cost")
ax2.set_ylabel("Number of Apartments")
ax2.axvline(float(manhattan_median), color="red", linestyle="dashed", linewidth=3, label="Median")
ax2.axvline(float(manhattan_mean), color="black", linestyle="dotted", linewidth=3, label="Mean")
ax2.axvline(statistics.mode(manhattan_price), color="orange", linestyle="solid", linewidth=3, label="Mode")
ax2.legend()

# --- Queens ---
ax3.hist(queens_price, range=(0, 10000), bins=14)
ax3.set_title("Queens Apartments Prices")
ax3.set_xlabel("Cost")
ax3.set_ylabel("Number of Apartments")
ax3.axvline(float(queens_median), color="red", linestyle="dashed", linewidth=3, label="Median")
ax3.axvline(float(queens_mean), color="black", linestyle="dotted", linewidth=3, label="Mean")
ax3.axvline(statistics.mode(queens_price), color="orange", linestyle="solid", linewidth=3, label="Mode")
ax3.legend()

plt.show()


#11. The price for the apartments is the most in Manhattan, and the least in Queens.

#12. The data is centered around the averages of each borough as the median, mode, and mean are not that spaced from one another.
# While the mode is not the most important indicator of centrality, the fact that mean, median, and mode are within a few hundred dollars for each borough indicates the data is centered around:
#
# $3,300 for Brooklyn
# $3,900 for Manhattan
# $2,300 for Queens

#13. The histograms of each borough shows how close the mean, medians, and modes are of each other, basically, in one observation bar.

# Mean
print("The mean price in Brooklyn is " + str(round(brooklyn_mean, 2)))
print("The mean price in Manhattan is " + str(round(manhattan_mean, 2)))
print("The mean price in Queens is " + str(round(queens_mean, 2)))

# Median
print("The median price in Brooklyn is " + str(brooklyn_median))
print("The median price in Manhattan is " + str(manhattan_median))
print("The median price in Queens is " + str(queens_median))

# Mode
print("The mode price in Brooklyn is " + str(brooklyn_mode[0]) + " and it appears " + str(
    brooklyn_mode[1]) + " times out of " + str(len(brooklyn_price)))
print("The mode price in Manhattan is " + str(manhattan_mode[0]) + " and it appears " + str(
    manhattan_mode[1]) + " times out of " + str(len(manhattan_price)))
print("The mode price in Queens is " + str(queens_mode[0]) + " and it appears " + str(
    queens_mode[1]) + " times out of " + str(len(queens_price)))