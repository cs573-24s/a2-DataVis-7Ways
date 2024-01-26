import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("penglings.csv")
df = df.dropna()

fig = px.scatter(
    df,
    x='flipper_length_mm',
    y='body_mass_g',
    color='species',
    size='bill_length_mm',
    opacity=0.8,
    labels={'flipper_length_mm': 'Flipper Length (mm)', 'body_mass_g': 'Body Mass (g)'}
)


fig.show()

print(df.head())
