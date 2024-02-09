# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 23:49:48 2024

@author: madel
"""

import pandas as pd

penglings = pd.read_csv(r'C:\Users\madel\Desktop\Spring 2024\Data Vis\Assignment 2\penglings.csv')


def assign_colors(dataframe, categorical_column, color_column):

    unique_categories = dataframe[categorical_column].unique()


    color_mapping = {
        'Adelie': 'red',
        'Gentoo': 'blue',
        'Chinstrap': 'green',

    }


    dataframe[color_column] = dataframe[categorical_column].map(color_mapping)

    return dataframe


pengligns = assign_colors(penglings, 'species', 'color_column')

# Display the updated DataFrame
print(penglings)

plt = penglings.plot.scatter(x='flipper_length_mm',
                      y='body_mass_g',
                      c='color_column', s='bill_length_mm', title="Pengling Flipper Length by Body Mass", alpha=0.8)