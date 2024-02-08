import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

data = pd.read_csv('C:/Users/nhein/Documents/Data Visualization/a2-DataVis-7Ways/python_matplotlib/penglings.csv')


colors_column = data["species"].map({'Adelie': 'orange', 'Chinstrap': 'purple', 'Gentoo': 'green'})

plt.scatter(
    data["flipper_length_mm"], 
    data["body_mass_g"], 
    s=data["bill_length_mm"] * 2,
    c=colors_column, 
    alpha = 0.5)
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")


def on_hover(sel):
    ind = sel.target.index
    x = data["flipper_length_mm"].iloc[ind]
    y = data["body_mass_g"].iloc[ind]
    size = data["bill_length_mm"].iloc[ind]
    species = data["species"].iloc[ind]
    island = data["island"].iloc[ind]
    sex = data["sex"].iloc[ind]

    sel.annotation.set_text(f"Species: {species}\nIsland: {island}\nFlipper Length: {x}\nBody Mass: {y}\nBill Length: {size} \nSex: {sex}")

mplcursors.cursor(hover=True).connect("add", on_hover)

plt.show()