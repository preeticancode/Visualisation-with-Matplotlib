import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("titanic2.csv")


ages_by_survival = {
    "Died": data.loc[data["Survived"] == 0, "Age"].dropna().tolist(),
    "Survived": data.loc[data["Survived"] == 1, "Age"].dropna().tolist()
}


fig, ax = plt.subplots(figsize=(8, 6))


ax.boxplot(
    ages_by_survival.values(),
    labels=ages_by_survival.keys(),
    showmeans=True,
    meanline=True
)


ax.set_title("Box Plots of Ages by Survival Status")
ax.set_ylabel("Age")
ax.grid(axis="y")


plt.savefig("exercise1_boxplots.png")
