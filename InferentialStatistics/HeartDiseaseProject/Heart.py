import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, binomtest

# The full dataset has been loaded for you as heart, then split into two subsets:
# yes_hd, which contains data for patients with heart disease
# no_hd, which contains data for patients without heart disease
heart = pd.read_csv("heart_disease.csv")
yes_hd = heart[heart["heart_disease"] == "presence"]
no_hd = heart[heart["heart_disease"] == "absence"]

# For this project, we’ll investigate the following variables:
# chol: serum cholesterol in mg/dl
# fbs: An indicator for whether fasting blood sugar is greater than 120 mg/dl (1 = true; 0 = false)

# Task-1: To start, we’ll investigate cholesterol levels for patients with heart disease.
chol_hd = yes_hd["chol"]

# Task-2: Calculate the mean cholesterol level for patients who were diagnosed with heart disease.
# Is it higher than 240 mg/dl?
yes_hd_chol = np.mean(chol_hd)
print(yes_hd_chol) # 251.41 > 240

# Task-3: Do people with heart disease have high cholesterol levels (greater than or equal to 240 mg/dl) on average?
# Test the following null and alternative hypotheses:
# Null: People with heart disease have an average cholesterol level equal to 240 mg/dl.
# Alternative: People with heart disease have an average cholesterol level that is greater than 240 mg/dl.
stat, pval = ttest_1samp(chol_hd, 240)
print(f"Probability of people with heart disease having cholesterol levels over 240 is {pval / 2 :.3f}.")
# When you divide the p-value by two (in order to run the one-sided test), you should get a p-value of 0.004.

# Task-4: Answer to the 3th task.
# This is less than 0.05, suggesting that heart disease patients have an average cholesterol level significantly higher than 240 mg/dl.

# Task-5:
# Repeat steps 1-4 in order to run the same hypothesis test, but for patients in the sample who were not diagnosed with heart disease.
# Do patients without heart disease have average cholesterol levels significantly above 240 mg/dl?
chol_no = no_hd["chol"]
mean_nochol = np.mean(chol_no)
print(f"Mean cholesterol for patients without heart disease : {mean_nochol :.3f}")
stat, pval_no = ttest_1samp(chol_no, 240)
print(f"The cholesterol p-value for people without heart disease is {pval_no / 2 :.3f}.")
# The p-value less than significance threshold, so we still can't reject the null hypothesis.

# Task-6:
num_patients = len(heart)
print(f"Number of patients in heart dataset: {num_patients :.3f}")

# Task-7:
# Remember that the fbs column of this dataset indicates whether or not a patient’s fasting blood sugar was greater than
# 120 mg/dl (1 means that their fasting blood sugar was greater than 120 mg/dl; 0 means it was less than or equal to 120 mg/dl).
# Calculate the number of patients with fasting blood sugar greater than 120.

high_fbs = np.sum(heart["fbs"] == 1)
print(f"Number of patients with fbs greater than 120: {high_fbs :.2f}")

# Task-8:
# By some estimates, about 8% of the U.S. population had diabetes (diagnosed or undiagnosed) in 1988 when this data was collected.
# While there are multiple tests that contribute to a diabetes diagnosis, fasting blood sugar levels
# greater than 120 mg/dl can be indicative of diabetes (or at least, pre-diabetes).
# If this sample were representative of the population, approximately how many people would you expect to have diabetes?
# Calculate and print out this number.
diabetic = len(heart) * 0.08
print(f"Diabetic people: {diabetic :.3f}.")
# It is almost as half as people with blood sugar above 120 mg/dl

# Task-9:
# Does this sample come from a population in which the rate of fbs > 120 mg/dl is equal to 8%?
# You can use to test the following null and alternative hypotheses:
# Null: This sample was drawn from a population where 8% of people have fasting blood sugar > 120 mg/dl
# Alternative: This sample was drawn from a population where more than 8% of people have fasting blood sugar > 120 mg/dl
p_value = binomtest(k = high_fbs, n = num_patients, p = 0.08, alternative = "greater")
print("P_value:", p_value.pvalue)

# Task-10:
# The value is less than significance threshold: 0.05, p-value = 0.00004.
# So, this tells us that null hypothesis is true: The sample was likely drawn from a population
# where 8% of people have fasting blood sugar > 120 mg/dl.

