import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Load the CSV data
data = pd.read_csv('public/penglings.csv')
# Replace NaN values in 'bill_length_mm' with the median of the column
data['bill_length_mm'].fillna(data['bill_length_mm'].median(), inplace=True)

# Define species colors
species_colors = {
    'Adelie': '#FF9013',
    'Chinstrap': '#9932CC',
    'Gentoo': '#008A8B'
}

# Create the bubble chart
fig, ax = plt.subplots()
for species, group in data.groupby('species'):
    ax.scatter(group['flipper_length_mm'], group['body_mass_g'], s=group['bill_length_mm']*10, 
               label=species, color=species_colors[species], alpha=0.5)

# Customizing the plot
ax.set_xlabel('Flipper Length (mm)')
ax.set_ylabel('Body Mass (g)')

# Adjust axes limits
ax.set_xlim([169, 234])
ax.set_ylim([2500, 6500])

# Adding a custom legend for bill lengths
# Note: Adjusting markersize by the sqrt of the desired display size to match the scatter plot's size representation
bill_length_legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='40 mm', markerfacecolor='k', markersize=np.sqrt(40)*2),
    Line2D([0], [0], marker='o', color='w', label='50 mm', markerfacecolor='k', markersize=np.sqrt(50)*2)
]
bill_length_legend = ax.legend(handles=bill_length_legend_elements, title='Bill Length (mm)', loc='upper left', bbox_to_anchor=(1, 1))

# Creating smaller bubbles for the species legend below the bill length legend
# Adjusting markersize for smaller representation
species_legend_elements = [
    Line2D([0], [0], marker='o', color=species_colors['Adelie'], label='Adelie', markersize=5),
    Line2D([0], [0], marker='o', color=species_colors['Chinstrap'], label='Chinstrap', markersize=5),
    Line2D([0], [0], marker='o', color=species_colors['Gentoo'], label='Gentoo', markersize=5)
]
# Adjust the bbox_to_anchor to position the species legend below the bill length legend
species_legend = ax.legend(handles=species_legend_elements, title='species', loc='upper left', bbox_to_anchor=(1, 0.85))

# Add the bill length legend back after adding the species legend
ax.add_artist(bill_length_legend)

plt.show()
