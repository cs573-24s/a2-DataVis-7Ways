import plotly.express as px
import pandas as pd

# Load the penguins dataset
data = pd.read_csv("penglings.csv")

# Drop rows with 'nan' values in the specified columns
columns_to_check = ['flipper_length_mm', 'body_mass_g', 'bill_length_mm']
data = data.dropna(subset=columns_to_check)

# Normalize the bill length
min_bill_length = data["bill_length_mm"].min()
max_bill_length = data["bill_length_mm"].max()
data["normalized_bill_length"] = (data["bill_length_mm"] - min_bill_length) / (max_bill_length - min_bill_length)
data["scaled_sizes"] = data["normalized_bill_length"]

# this step isreally important otherwise always show sizes nan should be an integer
data["sizes"] = data["scaled_sizes"]

# Replace NaN values in 'sizes' with a default value (0) using the fillna method
data["sizes"].fillna(0, inplace=True)  # Replace NaN with 0

# Create scatter plot using Plotly Express
fig = px.scatter(data, x="flipper_length_mm", y="body_mass_g",
                 color="species", size="sizes",
                 color_discrete_map={"Adelie": "orange", "Gentoo": "green", "Chinstrap": "purple"},
                 labels={"flipper_length_mm": "Flipper Length (mm)", "body_mass_g": "Body Mass (g)"})

# Customize the layout
fig.update_layout(
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis_title="Flipper Length (mm)",
    yaxis_title="Body Mass (g)",
    legend=dict(title="Species"),
    showlegend=True
)

# Show the plot
fig.show()
