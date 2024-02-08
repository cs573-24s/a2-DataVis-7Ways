import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
    dfPeng.dropna(inplace=True)
    dfPeng.drop(dfPeng.columns[0], axis=1, inplace=True)
    print(dfPeng)

sns.set_theme(style='whitegrid')

f, ax = plt.subplots(figsize = (6.5, 6.5))
sns.despine(f, left=True, bottom=True)
penguins = ["Adelie", "Chinstrap", "Gentoo"]
sns.scatterplot(x="flipper_length_mm", y="body_mass_g",
                hue="species", size="bill_length_mm",
                palette="ch:r=-.2,d=.3_r",
                hue_order=penguins,
                sizes=(20, 60),
                data=dfPeng, ax=ax)

ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")

plt.show()