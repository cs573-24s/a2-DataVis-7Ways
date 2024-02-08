from plotnine import ggplot, aes, geom_point, scale_color_manual, labs
import pandas as pd

# Load the data from the CSV file into a DataFrame
df = pd.read_csv('penglings.csv')

# Remove rows with NA values in relevant columns
df = df.dropna(subset=['flipper_length_mm', 'body_mass_g'])

# Define colors for each species (you can extend this as needed)
colors = {'Adelie': 'blue', 'Gentoo': 'green', 'Chinstrap': 'red'}

# Plot
(
    ggplot(df, aes(x='flipper_length_mm', y='body_mass_g', color='species')) +
    geom_point() +
    scale_color_manual(values=colors) +
    labs(title='Flipper Length vs Body Mass', x='Flipper Length (mm)', y='Body Mass (g)')
).draw()
