import numpy as np
import pandas as pd

# Reading the data from the csv file
nyc_trees = pd.read_csv("nyc_trees_census.csv")

# Seeing the first four rows of the data
print(nyc_trees.head())

# Categorical variables
categorical_vars = ["status", "health", "spc_common", "neighborhood"]

# Get tree counts by neighborhoods (Nominal variables - Not ordered)
tree_counts = nyc_trees["neighborhood"].value_counts()
print(tree_counts)


# Ordinal variables (They can be ordered)
# finding unique column values for a column
tree_health_statuses = list(nyc_trees["health"].unique())
print(tree_health_statuses)

# The value at the top would be mode of the data set
most_tree_neigh = tree_counts.index[0]
print("The neighborhood with most trees: " + str(most_tree_neigh))

# We want to change the order from Best to Worst
correct_order = ["Good", "Fair", "Poor"]
nyc_trees["health"] = pd.Categorical(nyc_trees["health"], correct_order, ordered = True)
print(nyc_trees["health"].unique())

# We can also find the median category of the health column
median_index = np.median(nyc_trees["health"].cat.codes)
median_cat = correct_order[int(median_index)]
print("Median health status: " + str(median_cat))

# We can find mean diameter of the diameter variable, `trunk_diam`
mean_diam = np.average(nyc_trees["trunk_diam"])
print("The mean truck diameter: " + str(mean_diam))

# Get Mean Category of `tree_diam_category`
size_labels_ordered = ['Small (0-3in)', 'Medium (3-10in)', 'Medium-Large (10-18in)', 'Large (18-24in)','Very large (>24in)']
nyc_trees.tree_diam_category = pd.Categorical(nyc_trees["tree_diam_category"],size_labels_ordered, ordered=True)
mean_diam_cat = np.average(nyc_trees["tree_diam_category"].cat.codes)
print("The tree diameter mean: " + str(mean_diam_cat))

# Calculate 25th Percentile Category
p25_index = np.percentile(nyc_trees["tree_diam_category"].cat.codes, 25)
p25_tree_diam_category = size_labels_ordered[int(p25_index)]
print("The 25th percentile for tree_diam_category: " + str(p25_tree_diam_category))

# Calculate 75th Percentile Category
p75_index = np.percentile(nyc_trees["tree_diam_category"].cat.codes, 75)
p75_tree_diam_category = size_labels_ordered[int(p75_index)]
print("The 75th percentile for tree_diam_category: " + str(p75_tree_diam_category))

# There are two ways to calculate proportions:
prop1 = nyc_trees['status'].value_counts()/len(nyc_trees["status"])
print("The proportion of tree status: " + str(prop1))

# Using value_counts
tree_status_proportions = nyc_trees["status"].value_counts(normalize = True)
print(tree_status_proportions * 100)

# When calculating proportions, you have to keep the missing data in mind.
health_proportions = nyc_trees["health"].value_counts(normalize = True)
print(health_proportions * 100)

# Using normalize(dropna = False) also adds missing items to the proportion count
health_proportions_2 = nyc_trees["health"].value_counts(normalize = True, dropna = False)
print(health_proportions_2 * 100)

# Binary categorical variables only have two values:
# Yes/ No, True/False, or 0/1
# Frequency and Proportion of Living trees
living_frequency = (nyc_trees["status"] == "Alive").sum()
living_proportion = (nyc_trees["status"] == "Alive").mean()

print("The number of living trees: " + str(living_frequency))
print("The proportion of living trees: " + str(living_proportion * 100))
