# Importing required libraries
import numpy as np
from math import sin
import matplotlib.pyplot as plt

# Define the small change in x for numerical derivative approximation
dx = 0.05 # The smaller the dx value, the smooth the curve will be towards true derivative
# Define the function f(x) = sin(x)
def f(x):
    return sin(x)
# Create x values from 0 to 20 with a step of dx
sin_x = [x for x in np.arange(0, 20, dx)]
# Compute the y values by applying f(x) to each x
sin_y = [f(x) for x in np.arange(0, 20, dx)]
# Estimate the derivative of f(x) numerically using np.gradient
sin_deriv = np.gradient(sin_y, dx)
# Plot the original sine function
plt.plot(sin_x, sin_y)
# Plot its numerical derivative (which should approximate cos(x))
plt.plot(sin_x, sin_deriv)
# Display the plots
plt.show()
# Print a few values of x, f(x), and f'(x) for inspection
print("x:", sin_x[:5])
print("f(x):", sin_y[:5])
print("f'(x):", sin_deriv[:5])
