import altair as alt
import pandas as pd

data = pd.read_csv("a2-DataVis-7Ways/penglings.csv")
data = data.dropna()

chart = alt.Chart(data).mark_circle(opacity=0.8).encode(
    x=alt.X('flipper_length_mm', title='Flipper Length (mm)', axis=alt.Axis(tickCount=7), scale=alt.Scale(domain=[170, 235])),
    y=alt.Y('body_mass_g', title='Body Mass (g)', axis=alt.Axis(tickCount=4), scale=alt.Scale(domain=[2500, 6500])),
    color='species',
    size='bill_length_mm',
    tooltip=[
        alt.Tooltip('flipper_length_mm', title='Flipper Length (mm)'),
        alt.Tooltip('body_mass_g', title='Body Mass (g)'),
        alt.Tooltip('species', title='Species'),
        alt.Tooltip('bill_length_mm', title='Bill Length (mm)')
    ]
).properties(
    width=500,
    height=400
).interactive()

chart.save("PyVis2.html")

