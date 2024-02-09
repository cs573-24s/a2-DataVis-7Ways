import pandas as pd
import plotly.express as px

# Load the data from the CSV file into a DataFrame
df = pd.read_csv('penglings.csv')

# Remove rows with NA values in relevant columns
df = df.dropna(subset=['flipper_length_mm', 'body_mass_g'])

# Define colors for each species (you can extend this as needed)
colors = {'Adelie': 'blue', 'Gentoo': 'green', 'Chinstrap': 'red'}

# Plot
fig = px.scatter(df, x='flipper_length_mm', y='body_mass_g', color='species', color_discrete_map=colors,
                 title='Flipper Length vs Body Mass', labels={'flipper_length_mm': 'Flipper Length (mm)',
                                                              'body_mass_g': 'Body Mass (g)'})
fig.show()
