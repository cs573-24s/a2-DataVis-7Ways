import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file into a DataFrame
df = pd.read_csv('penglings.csv')

# Remove rows with NA values in relevant columns
df = df.dropna(subset=['bill_length_mm', 'bill_depth_mm'])

# Define colors for each species (you can extend this as needed)
colors = {'Adelie': 'blue', 'Gentoo': 'green', 'Chinstrap': 'red'}

# Plot 1: Bill Length vs Bill Depth for Adelie and Gentoo penguins
plt.figure(figsize=(8, 6))

adelie_data = df[df['species'] == 'Adelie']
gentoo_data = df[df['species'] == 'Gentoo']

plt.scatter(adelie_data['bill_length_mm'], adelie_data['bill_depth_mm'], label='Adelie', color='blue')
plt.scatter(gentoo_data['bill_length_mm'], gentoo_data['bill_depth_mm'], label='Gentoo', color='green')

plt.title('Bill Length vs Bill Depth (Adelie, Gentoo)')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: Bill Length vs Bill Depth for Adelie and Chinstrap penguins
plt.figure(figsize=(8, 6))

adelie_data = df[df['species'] == 'Adelie']
chinstrap_data = df[df['species'] == 'Chinstrap']

plt.scatter(adelie_data['bill_length_mm'], adelie_data['bill_depth_mm'], label='Adelie', color='blue')
plt.scatter(chinstrap_data['bill_length_mm'], chinstrap_data['bill_depth_mm'], label='Chinstrap', color='red')

plt.title('Bill Length vs Bill Depth (Adelie, Chinstrap)')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')
plt.legend()
plt.grid(True)
plt.show()

# Plot 3: Bill Length vs Bill Depth for Gentoo and Chinstrap penguins
plt.figure(figsize=(8, 6))

gentoo_data = df[df['species'] == 'Gentoo']
chinstrap_data = df[df['species'] == 'Chinstrap']

plt.scatter(gentoo_data['bill_length_mm'], gentoo_data['bill_depth_mm'], label='Gentoo', color='green')
plt.scatter(chinstrap_data['bill_length_mm'], chinstrap_data['bill_depth_mm'], label='Chinstrap', color='red')

plt.title('Bill Length vs Bill Depth (Gentoo, Chinstrap)')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')
plt.legend()
plt.grid(True)
plt.show()

# Plot 4: Bill Length vs Bill Depth for all three species
plt.figure(figsize=(8, 6))

adelie_data = df[df['species'] == 'Adelie']
gentoo_data = df[df['species'] == 'Gentoo']
chinstrap_data = df[df['species'] == 'Chinstrap']

plt.scatter(adelie_data['bill_length_mm'], adelie_data['bill_depth_mm'], label='Adelie', color='blue')
plt.scatter(gentoo_data['bill_length_mm'], gentoo_data['bill_depth_mm'], label='Gentoo', color='green')
plt.scatter(chinstrap_data['bill_length_mm'], chinstrap_data['bill_depth_mm'], label='Chinstrap', color='red')

plt.title('Bill Length vs Bill Depth (All Species)')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')
plt.legend()
plt.grid(True)
plt.show()
