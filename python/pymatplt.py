import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file into a DataFrame
df = pd.read_csv('penglings.csv')

# Remove rows with NA values in relevant columns
df = df.dropna(subset=['flipper_length_mm', 'body_mass_g'])

# Define colors for each species (you can extend this as needed)
colors = {'Adelie': 'blue', 'Gentoo': 'green', 'Chinstrap': 'red'}

# Plot
plt.figure(figsize=(8, 6))

for species, color in colors.items():
    species_data = df[df['species'] == species]
    plt.scatter(species_data['flipper_length_mm'],
                species_data['body_mass_g'],
                label=species,
                color=color)

plt.title('Flipper Length vs Body Mass')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.legend()
plt.grid(True)
plt.show()
