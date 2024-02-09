import pandas as pd
import altair as alt

# Load the data from the CSV file into a DataFrame
df = pd.read_csv('penglings.csv')

# Remove rows with NA values in relevant columns
df = df.dropna(subset=['bill_length_mm', 'bill_depth_mm'])

# Define colors for each species (you can extend this as needed)
colors = {'Adelie': 'blue', 'Gentoo': 'green', 'Chinstrap': 'red'}

# Plot 1: Bill Length vs Bill Depth for Adelie and Gentoo penguins
chart1 = alt.Chart(df[(df['species'] == 'Adelie') | (df['species'] == 'Gentoo')]).mark_circle(size=60).encode(
    x='bill_length_mm',
    y='bill_depth_mm',
    color=alt.Color('species', scale=alt.Scale(domain=list(colors.keys()), range=list(colors.values()))),
    tooltip=['species', 'bill_length_mm', 'bill_depth_mm']
).properties(
    width=400,
    height=300,
    title='Bill Length vs Bill Depth (Adelie, Gentoo)'
).interactive()

# Plot 2: Bill Length vs Bill Depth for Adelie and Chinstrap penguins
chart2 = alt.Chart(df[(df['species'] == 'Adelie') | (df['species'] == 'Chinstrap')]).mark_circle(size=60).encode(
    x='bill_length_mm',
    y='bill_depth_mm',
    color=alt.Color('species', scale=alt.Scale(domain=list(colors.keys()), range=list(colors.values()))),
    tooltip=['species', 'bill_length_mm', 'bill_depth_mm']
).properties(
    width=400,
    height=300,
    title='Bill Length vs Bill Depth (Adelie, Chinstrap)'
).interactive()

# Plot 3: Bill Length vs Bill Depth for Gentoo and Chinstrap penguins
chart3 = alt.Chart(df[(df['species'] == 'Gentoo') | (df['species'] == 'Chinstrap')]).mark_circle(size=60).encode(
    x='bill_length_mm',
    y='bill_depth_mm',
    color=alt.Color('species', scale=alt.Scale(domain=list(colors.keys()), range=list(colors.values()))),
    tooltip=['species', 'bill_length_mm', 'bill_depth_mm']
).properties(
    width=400,
    height=300,
    title='Bill Length vs Bill Depth (Gentoo, Chinstrap)'
).interactive()

# Plot 4: Bill Length vs Bill Depth for all three species
chart4 = alt.Chart(df).mark_circle(size=60).encode(
    x='bill_length_mm',
    y='bill_depth_mm',
    color=alt.Color('species', scale=alt.Scale(domain=list(colors.keys()), range=list(colors.values()))),
    tooltip=['species', 'bill_length_mm', 'bill_depth_mm']
).properties(
    width=400,
    height=300,
    title='Bill Length vs Bill Depth (All Species)'
).interactive()

# Combine and display the charts
(chart1 | chart2).save('output1.html') & (chart3 | chart4).save('output2.html')
