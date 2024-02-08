from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10  # A palette suitable for up to 10 unique categories
import os
import pandas as pd

wd =  os.getcwd()
data = pd.read_csv(wd + "\penglings.csv")
#Drop NAs
data = data.dropna(subset=['bill_length_mm'])


species_list = data['species'].unique().tolist()
color_mapper = factor_cmap('species', palette=Category10[len(species_list)], factors=species_list)
data['scaled_size'] = (data['bill_length_mm']*data['bill_length_mm'])/120
p = figure(title="Assignment 2 - Python Bokeh", x_axis_label='Flipper Length (mm)', y_axis_label='Body Mass (g)', width=600, height=400)

source = ColumnDataSource(data)
p.circle('flipper_length_mm', 'body_mass_g', source=source, size='scaled_size',
         color=color_mapper, legend_field='species', fill_alpha=0.6)

# Customize tooltips
hover = HoverTool()
hover.tooltips = [
    ("Species", "@species"),
    ("Flipper Length", "@flipper_length_mm mm"),
    ("Body Mass", "@body_mass_g g"),
    ("Bill Length", "@bill_length_mm mm"),
]
p.add_tools(hover)

p.legend.location = "top_left"
output_file("bokeh.html")

# Show the plot
show(p)
