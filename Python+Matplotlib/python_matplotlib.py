import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import pandas as pd

# loading the csv as a dataframe
data = pd.read_csv('./penglings.csv')
flipper_length = data['flipper_length_mm']
body_mass_g = data['body_mass_g']
species = data['species']
bill_length = data['bill_length_mm']

# zip the different columns and iterate through each row collectively
# then go through the elements in each and plot accordingly
for s, f, b, bl in zip(species, flipper_length, body_mass_g, bill_length):
    if s == "Adelie":
        if bl < 40:
            plt.scatter(f, b, color='orange', alpha=0.6, edgecolors='orange', s=30)
        elif bl >= 40 and bl < 50:
            plt.scatter(f, b, color='orange', alpha=0.6, edgecolors='orange', s=100)
        else:
            plt.scatter(f, b, color='orange', alpha=0.6, edgecolors='orange', s=200)
    elif s == "Chinstrap":
        if bl < 40:
            plt.scatter(f, b, color='purple', alpha=0.6, edgecolors='purple', s=30)
        elif bl >= 40 and bl < 50:
            plt.scatter(f, b, color='purple', alpha=0.6, edgecolors='purple', s=100)
        else:
            plt.scatter(f, b, color='purple', alpha=0.6, edgecolors='purple', s=200)
    elif s == "Gentoo":
         if bl < 40:
            plt.scatter(f, b, color='Green', alpha=0.6, edgecolors='Green', s=30)
         elif bl >= 40 and bl < 50:
            plt.scatter(f, b, color='Green', alpha=0.6, edgecolors='Green', s=100)
         else:
            plt.scatter(f, b, color='Green', alpha=0.6, edgecolors='Green', s=200)
     
# making legends for the species
Adelie_legend = mpatches.Patch(color='orange', label  = 'Adelie')
Chinstrap_legend = mpatches.Patch(color='purple', label  = 'Chinstrap')
Gentoo_legend = mpatches.Patch(color='green', label  = 'Gentoo')

# making legends for the bill length
size_30_legend = mlines.Line2D([], [], color="white", marker='o', markersize=6, markerfacecolor="slategray", label='<40 mm')
size_40_legend = mlines.Line2D([], [], color="white", marker='o', markersize=10, markerfacecolor="slategray", label='40 mm')
size_50_legend = mlines.Line2D([], [], color="white", marker='o', markersize=15, markerfacecolor="slategray", label='50 mm')

plt.legend(handles=[Adelie_legend, Chinstrap_legend, Gentoo_legend, size_30_legend, size_40_legend, size_50_legend], loc='lower right', fontsize='x-large')

# adding labels and titles
plt.xlabel('Flipepr Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('DataViz-7Ways - Python + Matplotlib')
plt.show()



