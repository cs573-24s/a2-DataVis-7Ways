import pandas as pd
import altair as alt

penglings = pd.read_csv('penglings.csv')

domain = ['Adelie', 'Chinstrap', 'Gentoo']
range1 = ['#FC7D0B', '#9D53F2', '#27AAB0']
range2 = ['#FC7D0B', '#1170AA', '#57606C']

chart1 = alt.Chart(penglings).mark_circle(opacity=0.8).encode(
    x= alt.X("flipper_length_mm").scale(domain=[168,235]).title("Flipper Length (mm)").axis(values=list(range(170,240,10))),
    y= alt.Y("body_mass_g").scale(domain=[2500,6500]).title("Body Mass (g)").axis(values=[3000, 4000, 5000, 6000]),
    size= alt.Size("bill_length_mm").scale(domain=[30,50]),
    color=alt.Color('species').scale(domain=domain, range=range1)
).properties(
    width=500,
    height=400
)

chart1.save('chart1.html')

chart2 = alt.Chart(penglings).mark_circle(opacity=0.8).encode(
    x= alt.X("flipper_length_mm").scale(domain=[168,235]).title("Flipper Length (mm)").axis(values=list(range(170,240,10))),
    y= alt.Y("body_mass_g").scale(domain=[2500,6500]).title("Body Mass (g)").axis(values=[3000, 4000, 5000, 6000]),
    size= alt.Size("bill_length_mm").scale(domain=[30,50]),
    color=alt.Color('species').scale(domain=domain, range=range2)
).properties(
    width=500,
    height=400
)

chart2.save('chart2.html')