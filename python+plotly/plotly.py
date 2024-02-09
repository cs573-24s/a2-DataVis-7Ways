import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('penglings.csv')

sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='species', size='bill_length_mm',
                style='species', alpha=0.8)
plt.show()
