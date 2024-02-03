import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('penglings.csv')

# Map species to different markers
markers = {'Adelie': 'o', 'Gentoo': 's', 'Chinstrap': '^'}

# Set up the plot
plt.figure(figsize=(10, 6))

# Iterate over species and plot scatter points
for species, data in df.groupby('species'):
    plt.scatter(data['flipper_length_mm'], data['body_mass_g'], label=species, marker=markers[species], s=data['bill_length_mm']*10, alpha=0.8)

# Customize legend and labels
plt.legend(title='species', loc='upper left')
plt.xlabel('flipper_length_mm')
plt.ylabel('Body Mass (g)')

# Show plot
plt.show()
