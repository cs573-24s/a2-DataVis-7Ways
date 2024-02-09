import plotly.express as px
import pandas as pd


data = pd.read_csv("penglings.csv")


columns_to_check = ['flipper_length_mm', 'body_mass_g', 'bill_length_mm']
data = data.dropna(subset=columns_to_check)


min_bill_length = data["bill_length_mm"].min()
max_bill_length = data["bill_length_mm"].max()
data["normalized_bill_length"] = (data["bill_length_mm"] - min_bill_length) / (max_bill_length - min_bill_length)
data["scaled_sizes"] = data["normalized_bill_length"]


data["sizes"] = data["scaled_sizes"]


data["sizes"].fillna(0, inplace=True) 


fig = px.scatter(data, x="flipper_length_mm", y="body_mass_g",
                 color="species", size="sizes",
                 color_discrete_map={"Adelie": "orange", "Gentoo": "green", "Chinstrap": "purple"},
                 labels={"flipper_length_mm": "Flipper Length (mm)", "body_mass_g": "Body Mass (g)"})


fig.update_layout(
    margin=dict(l=10, r=10, t=10, b=10),
    width=1000,  
    height=600,  
    xaxis_title="Flipper Length (mm)",
    yaxis_title="Body Mass (g)",
    legend=dict(title="Species"),
    showlegend=True
)


fig.add_annotation(xref="paper", yref="paper", x=1, y=0.5, text="Small Ball (bill length mm: 40)", showarrow=False, font=dict(color="black"))
fig.add_annotation(xref="paper", yref="paper", x=1, y=0.4, text="Large Ball (bill length mm: 50)", showarrow=False, font=dict(color="black"))


fig.show()