import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = '/Users/a981199/Desktop/data_visualize/A2/R/a2/penglings.csv'
data = pd.read_csv(file_path)

# Set up the plot
plt.figure(figsize=(10, 6))

# Scatterplot with upward-trending trendline
sns.scatterplot(x='flipper_length_mm', y='body_mass_g', hue='species', size='bill_length_mm',
                sizes=(10, 200), alpha=0.8, palette='viridis', data=data)

# Set non-zero starting point for scales
plt.xlim(left=data['flipper_length_mm'].min() - 5)
plt.ylim(bottom=data['body_mass_g'].min() - 5)

# Add labels and ticks
plt.xlabel('Flipper Length')
plt.ylabel('Body Mass')
plt.xticks(range(170, int(data['flipper_length_mm'].max()) + 10, 10))
plt.yticks(range(2500, int(data['body_mass_g'].max()) + 500, 500))

# Add a legend (if necessary)
plt.legend()

# Show the plot
plt.show()
