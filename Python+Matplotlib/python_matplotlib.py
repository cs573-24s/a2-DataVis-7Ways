import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import pandas as pd

# uncomment and run in juypter notebook for interactivity
# import mpld3
# import mpld3
# from mpld3 import plugins

# loading the csv as a dataframe
data = pd.read_csv('./penglings.csv')

# color mapping 
color_matching = {'Adelie': 'orange', 'Chinstrap': 'purple', 'Gentoo' : 'green'}
color = data['species'].map(color_matching)

# determining data point sizes
circle_sizes = [50, 200, 300]
size_conditions = [(data['bill_length_mm'] < 40), (data['bill_length_mm'] >= 40) & (data['bill_length_mm'] < 50), (data['bill_length_mm'] >= 50)]
data['circle_size'] = np.select(size_conditions, circle_sizes, default=10)

# plotting the points
figure, ax = plt.subplots()
scatter = ax.scatter(data['flipper_length_mm'], data['body_mass_g'], c=data['species'].map(color_matching),s= data['circle_size'], marker='o', alpha=0.7, label='')


# making legends for the species
Adelie_legend = mpatches.Patch(color='orange', label  = 'Adelie')
Chinstrap_legend = mpatches.Patch(color='purple', label  = 'Chinstrap')
Gentoo_legend = mpatches.Patch(color='green', label  = 'Gentoo')

# making legends for the bill length
size_30_legend = mlines.Line2D([], [], color="white", marker='o', markersize=6, markerfacecolor="slategray", label='<40 mm')
size_40_legend = mlines.Line2D([], [], color="white", marker='o', markersize=10, markerfacecolor="slategray", label='40 mm')
size_50_legend = mlines.Line2D([], [], color="white", marker='o', markersize=15, markerfacecolor="slategray", label='50 mm')

# making the legend handles 
plt.legend(handles=[Adelie_legend, Chinstrap_legend, Gentoo_legend, size_30_legend, size_40_legend, size_50_legend], loc='lower right', fontsize='x-large')

# adding labels and titles
plt.xlabel('Flipepr Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('DataViz-7Ways - Python + Matplotlib')
plt.show()

# run in juypter notebook for interactive
# tooltip = plugins.PointLabelTooltip(scatter, labels=list(data['bill_length_mm']))
# plugins.connect(figure, tooltip)

# mpld3.display(figure)

plt.show()
