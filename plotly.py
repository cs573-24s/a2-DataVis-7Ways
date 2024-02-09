import pandas as pd
import plotly.express as px

# Load the data
file_path = '/Users/a981199/Desktop/data_visualize/A2/R/a2/penglings.csv'
data = pd.read_csv(file_path)

# Create the scatterplot
fig = px.scatter(data, x='flipper_length_mm', y='body_mass_g', color='species',
                 size='bill_length_mm', opacity=0.8, template='plotly_dark',
                 title='Penguin Scatterplot', labels={'Flipper Length': 'Flipper Length (mm)', 'Body Mass': 'Body Mass (g)'})

# Customize layout
fig.update_xaxes(tick0=10, dtick=10)
fig.update_yaxes(tick0=10, dtick=10)
fig.update_layout(xaxis_title='Flipper Length', yaxis_title='Body Mass')

# Show the plot
fig.show()
