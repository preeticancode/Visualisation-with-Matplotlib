import matplotlib.pyplot as plt
import numpy as np

# Line plot data
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, color='blue', label='Sine Wave')
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Save as .png
plt.savefig('line_plot.png')
