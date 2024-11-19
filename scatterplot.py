import matplotlib.pyplot as plt
import numpy as np

# Scatter plot data
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='green', alpha=0.7)
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Save as .png
plt.savefig('scatter_plot.png')
