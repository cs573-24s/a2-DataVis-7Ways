import pandas as pd
import plotly.express as px

# Sample CSV data (replace this with your actual CSV data)
csv_data = """
species,flipper_length_mm,body_mass_g,bill_length_mm
Adelie,181,3750,39.1
Gentoo,215,5100,49.4
Chinstrap,200,3900,46
"""

# Load CSV data into a DataFrame
df = pd.read_csv(pd.compat.StringIO(csv_data))

# Plot scatterplot with legend
fig = px.scatter(df, x='flipper_length_mm', y='body_mass_g', color='species', size='bill_length_mm',
                 labels={'flipper_length_mm': 'Flipper Length (mm)', 'body_mass_g': 'Body Mass (g)'},
                 title='Penguin Scatterplot with Legend')

# Update marker opacity
fig.update_traces(marker=dict(opacity=0.8))

# Show plot
fig.show()
