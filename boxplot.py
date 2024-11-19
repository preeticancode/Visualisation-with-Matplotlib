import matplotlib.pyplot as plt
import numpy as np

# Box plot data
data = [7, 8, 5, 6, 9, 12, 4, 3, 10, 11]

plt.boxplot(data, patch_artist=True)
plt.title('Box Plot Example')
plt.ylabel('Values')

# Save as .png
plt.savefig('box_plot.png')
