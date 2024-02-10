import plotly.express as px
import pandas as pd

data = pd.read_csv("penglings.csv", index_col=0)
df = pd.DataFrame(data)

#set max size
df['dummy_column_for_size'] = 1

plt = px.scatter(df, x="flipper_length_mm", y='body_mass_g', color="species",
                 color_discrete_sequence=['red', 'yellow', 'blue'], size_max=15,
                 hover_data=["species", "flipper_length_mm", "body_mass_g"],
                 labels={
                     "flipper_length_mm": "Flipper Length (mm)",
                     "body_mass_g": "Body Mass (g)",
                     "species": "Species"
                 })
plt.show()