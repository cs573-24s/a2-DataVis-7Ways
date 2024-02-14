import plotly.express as px
import pandas as pd

data = pd.read_csv("C:\\Users\\DT\\PycharmProjects\\datavis\\python_matplotlib\\penglings.csv", index_col=0)
df = pd.DataFrame(data)
df['dummy_column_for_size'] = 1  # Use this column to set size_max

fig = px.scatter(
    df,
    x="flipper_length_mm",
    y="body_mass_g",
    color="species",
    color_discrete_sequence=["orange", "purple", "green"],
    size="dummy_column_for_size",
    size_max=15,
    hover_data=["species", "flipper_length_mm", "body_mass_g"],
    labels={
        "flipper_length_mm": "Flipper Length (mm)",
        "body_mass_g": "Body Mass (g)",
        "species": "Species",
    },
)
fig.show()