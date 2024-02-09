# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


penglings = pd.read_csv(r'C:\Users\madel\Desktop\Spring 2024\Data Vis\Assignment 2\penglings.csv')

# add a column that has the color associated with each species category

sns.scatterplot(x="flipper_length_mm", y="body_mass_g", data=penglings, size='bill_length_mm', alpha=0.8, hue='species').set(title="Pengling Body Mass by Flipper Length")






