import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models.tickers import SingleIntervalTicker
from bokeh.models import HoverTool

data = pd.read_csv("a2-DataVis-7Ways/penglings.csv").dropna()

colors = {'Adelie': 'blue', 'Gentoo': 'red', 'Chinstrap': 'green'}

p = figure(title="Scatterplot", x_axis_label="Flipper Length (mm)", y_axis_label="Body Mass (g)",
           sizing_mode="stretch_both")

p.xaxis.ticker = SingleIntervalTicker(interval=10)
p.yaxis.ticker = SingleIntervalTicker(interval=1000)

p.xaxis.axis_label_text_font_size = "14pt"
p.yaxis.axis_label_text_font_size = "14pt"

p.xaxis.major_label_text_font_size = "12pt"
p.yaxis.major_label_text_font_size = "12pt"

scatter_renderers = []
for species, color in colors.items():
    scatter_renderer = p.scatter('flipper_length_mm', 'body_mass_g', size='bill_length_mm', color=color, alpha=0.8, legend_label=species, source=data[data['species'] == species], line_color=None)
    scatter_renderers.append(scatter_renderer)

# Add hover tooltips
hover = HoverTool(renderers=scatter_renderers,
                  tooltips=[("Species", "@species"),
                            ("Flipper Length", "@flipper_length_mm (mm)"),
                            ("Body Mass", "@body_mass_g (g)"),
                            ("Bill Length", "@bill_length_mm (mm)")])
p.add_tools(hover)

show(p)

