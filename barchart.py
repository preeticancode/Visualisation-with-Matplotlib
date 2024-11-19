import matplotlib.pyplot as plt

# Bar chart data
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.bar(categories, values, color='orange')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Save as .png
plt.savefig('bar_chart.png')
