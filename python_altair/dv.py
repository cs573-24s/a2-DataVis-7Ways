import altair as alt
import pandas as pd


data_url = "C:\\Users\\DT\\PycharmProjects\\datavis\\python_matplotlib\\penglings.csv"
df = pd.read_csv(data_url).dropna()



x_axis_title = "Flipper Length (mm)"
y_axis_title = "Body Mass (g)"
size_column = 'bill_length_mm'
color_column = 'species'
domain = ["Adelie", "Chinstrap", "Gentoo"]
color_range = ["orange", "purple", "green"]


chart = alt.Chart(df).mark_circle().encode(
    x=alt.X('flipper_length_mm', title=x_axis_title, scale=alt.Scale(domain=[170, 230])),
    y=alt.Y('body_mass_g', title=y_axis_title, scale=alt.Scale(domain=[2500, 6500])),
    size=alt.Size(size_column, title=size_column),
    color=alt.Color(color_column, title=color_column, scale=alt.Scale(domain=domain, range=color_range)),
    tooltip=[color_column, 'flipper_length_mm', 'body_mass_g', size_column]
).configure_mark(opacity=0.8).interactive()



chart.save('chart.html', embed_options={'renderer':'svg'})



