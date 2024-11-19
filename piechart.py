import matplotlib.pyplot as plt

# Pie chart data
labels = ['A', 'B', 'C', 'D']
sizes = [20, 30, 25, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'green', 'yellow'])
plt.title('Pie Chart Example')

# Save as .png
plt.savefig('pie_chart.png')
