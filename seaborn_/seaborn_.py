import seaborn as sns
import matplotlib.pyplot as plt
import pandas

penglings = pandas.read_csv("../penglings.csv")


df = pandas.DataFrame(penglings)

colors = {'Adelie': 'orange', 'Chinstrap': 'purple', 'Gentoo': 'cyan'}
# sizes = list(map(lambda x: 50 if x>=50 else 30, penglings['bill_length_mm']))

# scatter plot
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(
    x='flipper_length_mm',
    y='body_mass_g',
    size='bill_length_mm',
    hue='species',
    palette=colors,
    data=df
)

plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Scatter Plot of Flipper Length vs. Body Mass')

def hover(event):
    in_scatter, idx = scatter_plot.contains(event)
    if in_scatter:
        print(penglings.iloc[idx['ind'][0]])
        
scatter_plot.canvas.mpl_connect('motion_notify_event', hover)           

plt.show()