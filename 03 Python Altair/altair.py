# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:35:45 2024

@author: oz_ge
"""

import os
import pandas as pd

wd =  os.getcwd()
data = pd.read_csv(wd + "\penglings.csv")
#Drop NAs
data = data.dropna(subset=['bill_length_mm'])

import altair as alt
alt.renderers.enable("html")

fig = alt.Chart(data, width=600, height=400).mark_circle().encode(
    x=alt.X('flipper_length_mm', 
            scale=alt.Scale(domain=[min(data['flipper_length_mm']) - 10, max(data['flipper_length_mm']) + 10]),
            title='Flipper Length (mm)'),  
    y=alt.Y('body_mass_g', 
            scale=alt.Scale(domain=[min(data['body_mass_g']) - 200, max(data['body_mass_g']) + 200]),
            title='Body Mass (g)'),  # Custom Y-axis title
    color=alt.Color('species', legend=alt.Legend(orient='top-left')),
    size=alt.Size('bill_length_mm', 
                  scale=alt.Scale(domain=[32, 60], range=[50, 300]), 
                  legend=None),
    tooltip=['species', 'flipper_length_mm', 'body_mass_g', 'bill_length_mm']
).properties(
    title='Assignment 2 - Python Altair',
    width=600,
    height=400
).interactive()


fig.save('altair.html')

