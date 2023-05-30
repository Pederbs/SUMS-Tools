import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scienceplots

plt.style.use(['science', 'no-latex'])

# Define the function to fit to the data
def func(x, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u):
    return a*np.exp(x)/(b*np.sin(x)+c*np.cos(x)+d*x**8)

# Define the x and y values for the battery voltage and percentage data
x = np.array([25.2, 24.9, 24.67, 24.49, 24.14, 23.9, 23.72, 23.48, 23.25, 23.13,
     23.01, 22.89, 22.77, 22.72, 22.6, 22.48, 22.36, 22.24, 22.12, 21.65, 19.64])
y = np.array([100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0])

# Perform the nonlinear regression using curve_fit
popt, pcov = curve_fit(func, x, y)

# Print the optimized parameters of the fitted curve
print('a:', popt[0])
print('b:', popt[1])
print('c:', popt[2])
print('d:', popt[3])

# Define the x values for the curve
x_fit = np.linspace(19, 27, 1000)

# Calculate the y values for the curve using the optimized parameters
y_fit = func(x_fit, *popt)

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(10, 4))

# Plot the battery voltage and percentage data with a solid red line
ax.plot(x, y, '-r', label='Expected Capacity Relationship')

# Plot the fitted curve with a solid green line
ax.plot(x_fit, y_fit, '-g', label='Fitted Curve')

# Set the x and y limits of the plot
ax.set_xlim([19, 27])
ax.set_ylim([-10, 110])

# Add axis labels and a title to the plot
ax.set_xlabel('Battery Voltage [V]')
ax.set_ylabel('Percentage [%]')
#ax.set_title('Battery Voltage vs. Percentage')

# Add grid lines to the plot
ax.grid(True)

# Add a legend to the plot
ax.legend()

# Display the plot
plt.show()
