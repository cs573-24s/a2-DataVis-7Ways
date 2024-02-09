import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Viridis256
from bokeh.transform import linear_cmap

# Load the data
file_path = '/Users/a981199/Desktop/data_visualize/A2/R/a2/penglings.csv'
data = pd.read_csv(file_path)

# Create a Bokeh ColumnDataSource
source = ColumnDataSource(data)

# Define a custom color palette (orange, purple, green)
custom_palette = ['#FFA500', '#800080', '#008000']

# Define color mapping to species using the custom palette
mapper = factor_cmap(field_name='species', palette=custom_palette, factors=data['species'].unique())

#size_mapper = linear_cmap(field_name='bill_length_mm', palette=Viridis256, low=data['bill_length_mm'].min(), high=data['bill_length_mm'].max())


# Set up the plot
p = figure(width=800, height=500, title='Penguin Scatterplot', x_axis_label='Flipper Length', y_axis_label='Body Mass')

# Create the scatterplot with a custom color
scatter = p.circle('flipper_length_mm',
                   'body_mass_g',
                   source=source,
                   fill_color=mapper,
                   legend_field='species',
                   line_color='black',
                   #size=size_mapper,
                   )

# Customize ticks and labels
p.xaxis.ticker = [i for i in range(170, int(data['flipper_length_mm'].max()) + 10, 10)]
p.yaxis.ticker = [i for i in range(3000, int(data['body_mass_g'].max()) + 500, 500)]

# Add colorbar
color_bar = p.legend[0]
p.add_layout(color_bar, 'right')

# Show the plot
show(p)
