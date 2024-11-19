import matplotlib.pyplot as plt
import numpy as np

# Heatmap data
data = np.random.rand(6, 6)

plt.imshow(data, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap Example')

# Save as .png
plt.savefig('heatmap.png')
