import plotly.express as px

# Load the data
file_path = '/Users/a981199/Desktop/data_visualize/A2/R/a2/penglings.csv'
data = pd.read_csv(file_path)

# Handle NaN values in 'size' column
data['bill_length_mm'] = data['bill_length_mm'].fillna(5)

# Create the scatterplot
fig = px.scatter(data, x='flipper_length_mm', y='body_mass_g', color='species',
                 size='bill_length_mm', opacity=0.8, template='plotly_dark',
                 title='Penguin Scatterplot', labels={'flipper_length_mm': 'Flipper Length (mm)', 'body_mass_g': 'Body Mass (g)'})

# Customize layout
fig.update_xaxes(tick0=170, dtick=10)
fig.update_yaxes(tick0=3000, dtick=500)
fig.update_layout(xaxis_title='Flipper Length', yaxis_title='Body Mass')

# Show the plot
fig.show()
