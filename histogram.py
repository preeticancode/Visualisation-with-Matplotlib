import matplotlib.pyplot as plt
import numpy as np

# Histogram data
data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Save as .png
plt.savefig('histogram.png')
