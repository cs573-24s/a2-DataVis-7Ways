import pandas as pd
import plotly.express as px

# Load the CSV data
data = pd.read_csv('public/penglings.csv')  # Adjust the path to your CSV file
# Replace NaN values in 'bill_length_mm' with the median of the column
data['bill_length_mm'].fillna(data['bill_length_mm'].median(), inplace=True)

# Define species colors
species_colors = {
    'Adelie': 'rgba(255, 144, 19, 0.5)',
    'Chinstrap': 'rgba(153, 50, 204, 0.5)',
    'Gentoo': 'rgba(0, 138, 139, 0.5)'
}

# Create the bubble chart
fig = px.scatter(data, x='flipper_length_mm', y='body_mass_g',
                 size='bill_length_mm',
                 color='species',
                 color_discrete_map=species_colors,
                 hover_name='species')

# Update marker properties to remove white outlines
fig.update_traces(marker=dict(line=dict(width=0)))

# Update layout to customize axis titles
fig.update_layout(
    title=None,
    xaxis_title='Flipper Length (mm)',
    yaxis_title='Body Mass (g)',
    legend_title='species',
    legend=dict(title_side='top', y=0.5)  # Adjust legend position
)

# Adjust axes limits
fig.update_xaxes(range=[169, 234])
fig.update_yaxes(range=[2500, 6500])

# Manual addition of a secondary "legend" for bill_length_mm
fig.add_annotation(x=1.2, y=0.69, xref='paper', yref='paper',
                   text="Bill Length (mm)", showarrow=False, align='left')
fig.add_annotation(x=1.2, y=0.64, xref='paper', yref='paper',
                   text="40", showarrow=False)
fig.add_annotation(x=1.2, y=0.59, xref='paper', yref='paper',
                   text="50", showarrow=False)

# Correcting shapes to be circles by ensuring equal x and y dimensions
# The size of the circles can be adjusted by changing the x0, y0, x1, y1 values
fig.add_shape(type="circle", xref="paper", yref="paper",
              x0=1.15, y0=0.625, x1=1.17, y1=0.655, 
              line_color="black", fillcolor="black")
fig.add_shape(type="circle", xref="paper", yref="paper",
              x0=1.1475, y0=0.573, x1=1.1725, y1=0.608,
              line_color="black", fillcolor="black")

# Adjust layout for the shapes and annotations
fig.update_layout(
    margin=dict(l=0, r=250, t=0, b=0)  # Adjust right margin to accommodate secondary legend
)

# Show the plot
fig.show()
