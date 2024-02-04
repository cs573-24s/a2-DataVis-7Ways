import pandas as pd
import altair as alt
import altair_viewer
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

chart = alt.Chart(dfPeng).mark_point().encode(
    x = "flipper_length_mm",
    y = "body_mass_g",
    color = "species"
).interactive()

# altair_viewer.display(chart)
chart.show()
# print(chart)


