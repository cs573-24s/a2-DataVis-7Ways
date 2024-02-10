import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


penglings = pd.read_csv("penglings.csv", index_col=0)

df = pd.DataFrame(penglings)

colors = ['red', 'yellow', 'blue']
ax = sns.relplot(data=df, x="flipper_length_mm", y='body_mass_g', hue="species", alpha=0.8, palette=colors)
ax.set(xlabel='Flipper Length (mm)', ylabel='Body Mass(g)')
plt.show()