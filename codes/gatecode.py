import numpy as np
import matplotlib.pyplot as plt

# Function definition
def my_function(t, k):
    return k * (1 - np.exp(-2 * t)) / 2

# Values for t
t_values = np.linspace(0, 5, 100)  # You can adjust the range and number of points as needed

# Values for k
k_values = [1, 2, 3]

# Plotting the function for each value of k
for k in k_values:
    plt.plot(t_values, my_function(t_values, k), label=f'k = {k}')

# Adding labels and title
plt.xlabel('t')
plt.ylabel('g(t)')
plt.legend()

# Adding grid
plt.grid(True)

# Display the plot
plt.savefig('gate.png')

