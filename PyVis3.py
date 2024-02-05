import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("a2-DataVis-7Ways/penglings.csv")
data = data.dropna()

colors = {'Adelie': 'blue', 'Gentoo': 'red', 'Chinstrap':'green'}

plt.scatter(data['flipper_length_mm'], data['body_mass_g'], s=data['bill_length_mm'], c=data['species'].map(colors), alpha=0.8)

for species, color in colors.items():
    plt.scatter([], [], c=color, label=species)  # Empty scatter plot for creating legend

plt.legend()

plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')



plt.show()