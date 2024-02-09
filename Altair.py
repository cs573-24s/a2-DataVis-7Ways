import altair as alt
import pandas as pd
import webbrowser

# Load the data
data = pd.read_csv("/Users/a981199/Desktop/data_visualize/A2/R/a2/penglings.csv")

# Enable Altair to work with Jupyter Notebook
alt.renderers.enable('default')

# Define custom colors for each species
color_scale = alt.Color('species:N', scale=alt.Scale(
    domain=['Adelie', 'Chinstrap', 'Gentoo'],
    range=['orange', 'purple', 'green']
))

# Create the scatter plot with custom color scale
scatter_plot = alt.Chart(data).mark_circle(opacity=0.8).encode(
    x=alt.X('flipper_length_mm:Q', title='Flipper Length', scale=alt.Scale(zero=False)),
    y=alt.Y('body_mass_g:Q', title='Body Mass', scale=alt.Scale(zero=False)),
    color=color_scale,
    size='bill_length_mm:Q',
    tooltip=['species:N', 'flipper_length_mm:Q', 'body_mass_g:Q', 'bill_length_mm:Q']
).properties(
    width=600,
    height=400
)

# Save the chart as an HTML file
chart_file_path = "/Users/a981199/Desktop/data_visualize/A2/R/a2/scatter_plot.html"
scatter_plot.save(chart_file_path)

# Open the default web browser to display the chart
webbrowser.open('file://' + chart_file_path, new=2)

