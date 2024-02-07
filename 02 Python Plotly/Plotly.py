# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:04:11 2024

@author: oz_ge
"""

import os
import pandas as pd

wd =  os.getcwd()
data = pd.read_csv(wd + "\penglings.csv")
#Drop NAs
data = data.dropna(subset=['bill_length_mm'])
data['scaled_size'] = (data['bill_length_mm']*data['bill_length_mm'])

import plotly.io as pio
import plotly.express as px
pio.renderers.default='browser'

fig = px.scatter(data, x="flipper_length_mm", y="body_mass_g", color="species",
                 size='scaled_size', hover_data=['species'],
                 labels={
                     "flipper_length_mm": "Flipper Length (mm)",
                     "body_mass_g": "Body Mass (g)",
                     "species": "Species"
                 },)
fig.update_layout(title='Assignment 2 - Scatter Plot with Python Plotly')
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.95,
    xanchor="left",
    x=0.05
))

fig.show()


