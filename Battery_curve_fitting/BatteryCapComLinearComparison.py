import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'no-latex'])

# Define the x and y values for the linear function
x1 = [19.8, 25.5]
y1 = [0, 100]

# Define the x and y values for the battery voltage and percentage data
x2 = [25.2, 24.9, 24.67, 24.49, 24.14, 23.9, 23.72, 23.48, 23.25, 23.13,
     23.01, 22.89, 22.77, 22.72, 22.6, 22.48, 22.36, 22.24, 22.12, 21.65, 19.64]
y2 = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(10, 4))

# Plot the linear function with a solid blue line
ax.plot(x1, y1, '-b', label='Linear Function')

# Plot the battery voltage and percentage data with a solid red line
ax.plot(x2, y2, '-r', label='Expected Capacity Relationship')

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
