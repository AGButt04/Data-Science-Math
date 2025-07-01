import numpy as np
import matplotlib.pyplot as plt
import pylab as p

# Calculating variance in a dataset

grades = [88, 82, 85, 84, 90]
grades_mean = np.mean(grades)

# formula:
#   difference = (X - u (mean))^2
#   We have to calculate this for each point in dataset and sum the values
#   var = difference_sum/N --> N = len(dataset)

sum_difference = 0
for grade in grades:
    sum_difference += (grade - grades_mean) ** 2

# Divide the sum by the length of the set to find variance
variance = sum_difference / len(grades)

print(f"The variance of grades is {variance}.")

# NumPy also has a variance function.
teacher_one_grades = [80.24, 81.15, 81.29, 82.12, 82.52, 82.54, 82.76, 83.37, 83.42, 83.45,
                      83.47, 83.79, 83.91, 83.98, 84.03, 84.69, 84.74, 84.89, 84.95, 84.95,
                      85.02, 85.18, 85.53, 86.29, 86.83, 87.29, 87.47, 87.62, 88.04, 88.5]
teacher_two_grades = [65.82, 70.77, 71.46, 73.63, 74.62, 76.53, 76.86, 77.06, 78.46, 79.81,
                      80.64, 81.61, 81.84, 83.67, 84.44, 84.73, 84.74, 85.15, 86.55, 88.06,
                      88.53, 90.12, 91.27, 91.62, 92.86, 94.37, 95.64, 95.99, 97.69, 104.4]

teacher_one_var = p.var(teacher_one_grades)
teacher_two_var = p.var(teacher_two_grades)

# Create figure with 2 subplots (vertically stacked), and control spacing
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))  # wider and taller figure

# Adjust vertical space between subplots
fig.subplots_adjust(hspace=0.5)  # space between top and bottom (0.5 is good spacing)

# Plot for Teacher One
ax1.hist(teacher_one_grades)
ax1.set_title("Teacher One Grades")
ax1.set_xlabel("Grades")
ax1.set_xlim(65, 105)

# Plot for Teacher Two
ax2.hist(teacher_two_grades, bins=20)
ax2.set_title("Teacher Two Grades")
ax2.set_xlabel("Grades")
ax2.set_xlim(65, 105)

plt.show()

#As we can see, the variance of teacher two is clearly more than teacher one
# Variance is useful because it is a measure of spread. While we might get a
# general understanding of the spread by looking at a histogram, computing the
# variance gives us a numerical value that helps us describe the level of confidence of our comparison.