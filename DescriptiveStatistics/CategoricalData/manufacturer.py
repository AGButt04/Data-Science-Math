import pandas as pd
import numpy as np

# Read in the data from csv
car_eval = pd.read_csv("car_eval_dataset.csv")

# Let's do some small tasks on this data set

# Task 1:
# Create a table of frequencies of all the cars reviewed by manufacturer_country.
# What is the modal category? Which country appears 4th most frequently?
manufacturer_country = car_eval["manufacturer_country"].value_counts()
print(manufacturer_country)
# 1st is Japan (modal country) and 4th is USA

# Task 2:
# Calculate a table of proportions for countries that appear in manufacturer_country in the dataset.
# What percentage of cars were manufactured in Japan?
proportion_table = car_eval["manufacturer_country"].value_counts(normalize = True)
print(proportion_table * 100)
# 22.8% cars are being manufactured in Japan.

# Task 3:
# buying_cost is a categorical variable which describes the cost of buying any car in the dataset.
# Print out a list of the possible values for this variable.
buying_cost = car_eval["buying_cost"].unique()
print(buying_cost)

# Task 4:
# buying_cost is an ordinal categorical variable, which means we can create an order associated with the values
# in the data and perform additional numeric operations on the variable. Create a new list, buying_cost_categories,
# that contains the unique values in buying_cost, ordered from lowest to highest.
buying_cost_categories = ["low", "med", "high", "vhigh"]

# Task 5:
# Convert buying_cost to type 'category' using the list you created in the previous exercise.
car_eval["buying_cost"] = pd.Categorical(car_eval["buying_cost"], buying_cost_categories, ordered = True)
print(car_eval["buying_cost"])

# Task 6:
# Calculate the median category of buying_cost variable
median_index = np.median(car_eval["buying_cost"].cat.codes)
median_cat = buying_cost_categories[int(median_index)]
print(f"The median category is {median_cat}.")

# Task 7:
# luggage is a categorical variable in the car evaluations dataset that records the luggage capacity
# for each reviewed car. Calculate a table of proportions for this variable and print the result
luggage_prop = car_eval["luggage"].value_counts(normalize = True)
print(luggage_prop * 100)

# Task 8:
#Are there any missing values in this column? Replicate the table of proportions from the previous exercise,
# but do not drop any missing values from the count. Print your result.
luggage_prop_2 = car_eval["luggage"].value_counts(normalize = True, dropna = False)
print(luggage_prop_2 * 100)

# Task 9:
#Without passing normalize = True to .value_counts(), can you replicate the result you got in the previous exercises?
prop_luggage = car_eval["luggage"].value_counts()/ len(car_eval["luggage"])
print(prop_luggage * 100)

# Task 10:
# doors is a categorical variable in the car evaluations dataset that records the count of doors for each reviewed car.
# Find the count of cars that have 5 or more doors.
five = np.sum(car_eval["doors"] == "5more")
print(f"The number of cars with 5+ doors: {five}.")

# Task 11:
# Proportion of cars with 5 plus doors
five_prop = np.mean(car_eval["doors"] == "5more")
print(f"The number of cars with 5+ doors: {five_prop * 100:.2f}%.")