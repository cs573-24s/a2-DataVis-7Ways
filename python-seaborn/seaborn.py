import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

data = pd.read_csv("penglings.csv", index_col=0)
df = pd.DataFrame(data)

colors = ["#F28C28", "#21908dff", "#BF40BF"]
ax = sns.relplot(data=df, x="flipper_length_mm", y='body_mass_g', hue="species", s=150, alpha=.8, palette=colors)
ax.set(xlabel='Flipper Length (mm)', ylabel='Body Mass(g)')