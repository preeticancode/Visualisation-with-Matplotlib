import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset
data = pd.read_csv("titanic2.csv")

# Filter the data to remove rows with missing Age or Fare values
filtered_data = data.dropna(subset=["Age", "Fare"])

# Prepare data for the visualizations
survival_dict = data["Survived"].value_counts().to_dict()
pclass_dict = data["Pclass"].value_counts().to_dict()
ages_list = filtered_data["Age"].tolist()  # Only non-NaN Age values
fares_list = filtered_data["Fare"].tolist()  # Only non-NaN Fare values

# Create the figure and axes for a 2x2 grid
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Visualization 1: Pie Chart (Survival Proportions)
axs[0, 0].pie(
    survival_dict.values(),
    labels=["Died", "Survived"],
    autopct="%.0f%%",
    colors=["red", "green"]
)
axs[0, 0].set_title("Survival Proportions")

# Visualization 2: Bar Chart (Passenger Class Distribution)
axs[0, 1].bar(
    pclass_dict.keys(),
    pclass_dict.values(),
    color=["gold", "silver", "#CD7F32"]
)
axs[0, 1].set_title("Passenger Class Distribution")
axs[0, 1].set_xlabel("Passenger Class")
axs[0, 1].set_ylabel("Number of Passengers")
axs[0, 1].grid(axis="y")

# Visualization 3: Histogram (Age Distribution)
bins = range(0, int(max(ages_list)) + 10, 10)
axs[1, 0].hist(
    ages_list,
    bins=bins,
    edgecolor="black",
    color="skyblue"
)
axs[1, 0].set_title("Age Distribution")
axs[1, 0].set_xlabel("Age")
axs[1, 0].set_ylabel("Frequency")
axs[1, 0].grid(axis="y")

# Visualization 4: Scatter Plot (Age vs. Fare)
axs[1, 1].scatter(
    x=ages_list,
    y=fares_list,
    marker=".",
    s=10,
    color="purple",
    alpha=0.7
)
axs[1, 1].set_title("Age vs. Fare")
axs[1, 1].set_xlabel("Age")
axs[1, 1].set_ylabel("Fare")
axs[1, 1].grid(axis="both")

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("exercise3_additional.png")
