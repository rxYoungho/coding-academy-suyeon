import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(3, 5, 0.01)

# Calculating mean and standard deviation
mean = statistics.mean(x_axis)

sd = statistics.stdev(x_axis)

plt.plot(x_axis, norm.pdf(x_axis, 4.65, 0.12),  label='Comfortable To Use')
plt.plot(x_axis, norm.pdf(x_axis, 4.45, 0.12),  label='Speed of Transaction')

x = np.array([4, 4, 4, 5])
y = np.array([0, 0, 0, 0])

plt.scatter(x, y)

plt.xlabel('Mean MOS')
plt.legend()

plt.show()
