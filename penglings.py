import pandas as pd
import altair as alt 

df = pd.read_csv('penglings.csv', index_col=0)

alt.Chart(df).mark_circle(size=60).encode(
    x='flipper_length_mm',
    y='body_mass_g',
    color='species',
    tooltip=['species', 'flipper_length_mm', 'body_mass_g']
).interactive()