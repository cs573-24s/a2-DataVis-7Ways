import pandas
import matplotlib.pyplot as plt

penglings = pandas.read_csv("../penglings.csv")

colors = {'Adelie': 'orange', 'Chinstrap': 'purple', 'Gentoo': 'cyan'}

# sizes =list(map(lambda x: 40 if x>=40 else 30, penglings['bill_length_mm']))

# Scatter plot
fig, ax = plt.subplots()

plot = ax.scatter(
    penglings['flipper_length_mm'],
    penglings['body_mass_g'],
    s=penglings['bill_length_mm'] * 2,  # bill_length_mm used for bubble size
    c=penglings['species'].map(colors),  # Map species to colors
    alpha=0.8  # Transparency
)
ax.set_xlabel('Flipper Length (mm)')
ax.set_ylabel('Body Mass (g)')

def hover(event):
    in_scatter, idx = plot.contains(event)
    if in_scatter:
        print(penglings.iloc[idx['ind'][0]])

# https://stackoverflow.com/questions/7908636/how-to-add-hovering-annotations-to-a-plot
fig.canvas.mpl_connect('motion_notify_event', hover)           

plt.show()