import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("titanic2.csv")


survival_by_gender = data[data["Survived"] == 1]["Sex"].value_counts().to_dict()
survival_by_class = data[data["Survived"] == 1]["Pclass"].value_counts().to_dict()
survival_by_embarkation = data[data["Survived"] == 1]["Embarked"].value_counts().to_dict()


fig, axs = plt.subplots(1, 3, figsize=(15, 5))


axs[0].pie(
    survival_by_gender.values(), 
    labels=survival_by_gender.keys(), 
    autopct="%.0f%%", 
    colors=['lightblue', 'pink']
)
axs[0].set_title("Survival by Gender")


axs[1].pie(
    survival_by_class.values(), 
    labels=survival_by_class.keys(), 
    autopct="%.0f%%", 
    colors=['gold', 'silver', '#CD7F32']
)
axs[1].set_title("Survival by Class")


axs[2].pie(
    survival_by_embarkation.values(), 
    labels=survival_by_embarkation.keys(), 
    autopct="%.0f%%"
)
axs[2].set_title("Survival by Embarkation")


plt.tight_layout()
plt.savefig("exercise2_piecharts.png")
