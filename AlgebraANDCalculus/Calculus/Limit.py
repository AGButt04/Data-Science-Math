import numpy as np
from math import sin, cos, log, pi
import matplotlib.pyplot as plt

# Function to approximate the derivative using the limit definition
def limit_derivative(f, x, h):
  """
  f: function to differentiate
  x: point at which to evaluate the derivative
  h: small interval approaching 0
  """
  sub = f(x + h) - f(x)  # Difference in function values
  return sub / h         # Divide by h to get the approximate derivative

# Define sample functions
def f1(x): return sin(x)                # f1(x) = sin(x)
def f2(x): return pow(x, 4)             # f2(x) = x^4
def f3(x): return pow(x, 2) * log(x)    # f3(x) = x^2 * log(x)

# Print approximate derivatives for sin(x) at x=1 using decreasing h values
print(limit_derivative(f1, x=1, h=2))        # Coarse approximation
print(limit_derivative(f1, x=1, h=0.1))      # Better approximation
print(limit_derivative(f1, x=1, h=0.00001))  # Very accurate approximation

# Plot the true derivative of f2(x) = x^4, which is f2'(x) = 4x^3
x_vals = np.linspace(1, 10, 200)
y_vals = [4 * pow(val, 3) for val in x_vals]  # Analytical derivative values
plt.figure(1)
plt.plot(x_vals, y_vals, label="True Derivative", linewidth=4)

# Function to plot approximated derivatives using the limit definition
def plot_approx_deriv(f):
  x_vals = np.linspace(1, 10, 200)
  h_vals = [10, 1, 0.25, 0.01]  # Different h values for testing accuracy

  for h in h_vals:
      derivative_values = [limit_derivative(f, x, h) for x in x_vals]
      plt.plot(x_vals, derivative_values, linestyle='--', label="h = " + str(h))

  plt.legend()
  plt.title("Convergence to Derivative by Varying h")
  plt.show()

# Plot approximated derivatives of f2(x) = x^4
plot_approx_deriv(f2)
