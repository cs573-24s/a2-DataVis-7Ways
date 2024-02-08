import plotly.express as px
import pandas as pd

df = pd.read_csv("a2-DataVis-7Ways/penglings.csv")
df = df.dropna()

fig = px.scatter(
    df,
    x='flipper_length_mm',
    y='body_mass_g',
    color='species',
    size='bill_length_mm',
    opacity=0.8,
    labels={'flipper_length_mm': 'Flipper Length (mm)', 'body_mass_g': 'Body Mass (g)', 'species':'Species', 'bill_length_mm':'Bill Length (mm)'}
)


fig.show()
