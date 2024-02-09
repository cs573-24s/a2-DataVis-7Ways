import altair as alt
import pandas as pd


data = pd.read_csv('penglings.csv')


color_scale = alt.Scale(domain=['Adelie', 'Gentoo', 'Chinstrap'],
                        range=['#FF4500', '#006400', '#4B0082'])


scatter_plot = alt.Chart(data).mark_circle(opacity=0.8).encode(
    x=alt.X('flipper_length_mm', title='Flipper Length (mm)', scale=alt.Scale(domain=[160, 240])),
    y=alt.Y('body_mass_g', title='Body Mass (g)', scale=alt.Scale(domain=[2500, 6500])),
    color=alt.Color('species', scale=color_scale),
    size='bill_length_mm'
).properties(
    width=500,
    height=500,
    title='Penguins ScatterPlot'
)

scatter_plot.save('scatter_plot.html')
