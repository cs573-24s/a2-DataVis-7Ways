#%%
import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\DT\\PycharmProjects\\datavis\\python_matplotlib\\penglings.csv", index_col=0)

df = pd.DataFrame(data)

# Define colors for each species
colors = {"Adelie": "orange", "Chinstrap": "purple", "Gentoo": "green"}

# Plot the scatter chart
fig, ax = plt.subplots()
ax.margins(0.05)  # Add padding

ax.scatter(
    df["flipper_length_mm"],
    df["body_mass_g"],
    c=df["species"].map(colors),
    alpha=0.5,
    s=100,
)

plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()
