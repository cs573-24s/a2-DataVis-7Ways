#%%
import pandas as pd

import matplotlib.pyplot as plt

#used as reference https://kanoki.org/2020/08/30/matplotlib-scatter-plot-color-by-category-in-python/
data = pd.read_csv("/penglings.csv", index_col=0)

df = pd.DataFrame(data)

colors = {'Adelie':'orange', "Chinstrap":'purple', 'Gentoo': 'teal'}


# Plot
fig, ax = plt.subplots()
ax.margins(0.05) # padding

ax.scatter(df['flipper_length_mm'], df['body_mass_g'], c=df['species'].map(colors), alpha=0.5, s=100)
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()
# %%
