import altair as alt
import pandas as pd
import numpy as np

# Set Altair theme
alt.themes.enable('quartz')

# Load data
data = pd.read_csv('penglings.csv')

# Calculate the min and max for flipper_length_mm and body_mass_g
min_flipper_length = data['flipper_length_mm'].min()
max_flipper_length = data['flipper_length_mm'].max()
min_body_mass = data['body_mass_g'].min()
max_body_mass = data['body_mass_g'].max()

# Generate tick values
x_ticks = np.arange(150, max_flipper_length + 10, 10)
y_ticks = np.arange(2000, max_body_mass + 1000, 1000)

# Define the scatter plot
scatter_plot = alt.Chart(data).mark_circle().encode(
    x=alt.X('flipper_length_mm:Q',
            scale=alt.Scale(domain=(170, 240)),
            axis=alt.Axis(values=list(x_ticks)),
            title='Flipper Length (mm)'),
    y=alt.Y('body_mass_g:Q',
            scale=alt.Scale(domain=(2000, 6500)),
            axis=alt.Axis(values=list(y_ticks)),
            title='Body Mass (g)'),
    color='species:N',
    size=alt.Size('bill_length_mm:Q', scale=alt.Scale(range=[20, 500]))
).properties(
    width=800,
    height=600,
    title={
        "text": ['Diving into Penguin Metrics'], 
        "subtitle": ['An Insight into Flipper Length and Body Mass Across Different Species'],
        "color": "black",
        "subtitleColor": "black"
    }
).configure_title(
    fontSize=24,
    font='Georgia', 
    anchor='start',
    color='black'
).configure_axis(
    labelFont='Georgia',  
    titleFont='Georgia'  
).configure_legend(
    titleColor='black',
    titleFontSize=14,
    labelColor='black',
    labelFontSize=12,
    labelFont='Georgia',
    titleFont='Georgia',
    padding=10,
    cornerRadius=5,
    symbolStrokeWidth=2
).configure_axis(
    grid=True  # Enabling grid lines
).configure_axisX(
    labelAngle=-45
).configure_view(
    strokeOpacity=0  # Removes the border around the plot
)

scatter_plot = scatter_plot.encode(
    tooltip=[
        alt.Tooltip('species:N', title='Species'),
        alt.Tooltip('flipper_length_mm:Q', title='Flipper Length (mm)'),
        alt.Tooltip('body_mass_g:Q', title='Body Mass (g)'),
        alt.Tooltip('bill_length_mm:Q', title='Bill Length (mm)')
    ]
)

#Interactive Selection
selection = alt.selection_point(fields=['species'])
scatter_plot = scatter_plot.add_params(
    selection
).encode(
    opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
)

#Zooming and panning
scatter_plot = scatter_plot.interactive()

# Display the plot
scatter_plot

# Save the plot as an HTML file
scatter_plot.save('scatter_plot.html')
