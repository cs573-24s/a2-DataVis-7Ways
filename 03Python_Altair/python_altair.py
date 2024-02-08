import pandas as pd
import altair as alt
alt.renderers.enable("mimetype") 


def read_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

csv_file_path = '/Users/danteamicarella/Documents/GitHub/a2-DataVis-7Ways/penglings.csv' 

dfPeng = read_csv(csv_file_path)

if dfPeng is not None:
    dfPeng.drop(dfPeng.columns[0], axis=1, inplace=True)
    print(dfPeng)

chart = alt.Chart(dfPeng).mark_point(opacity=.8, filled=True).encode( # opacity = .8
    x = alt.X("flipper_length_mm", scale=alt.Scale(domain=(170, 240)), title='Flipper Length (mm)'), # change the scale and the name
    y = alt.Y("body_mass_g", scale=alt.Scale(domain=(2500, 6500)), title='Body Mass (g)'),
    color = "species",
    size = "bill_length_mm",
    tooltip = ['species','sex','island'] # hover over element
).properties(
    width = 500,
    height= 500
).interactive().configure_axis(grid=False) # remove grid lines and make it interactive

chart.save('python_altair.html')

