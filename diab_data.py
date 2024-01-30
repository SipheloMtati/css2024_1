# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:29:53 2024

@author: s1500174
"""

import pandas

file_diab = pandas.read_csv("C:/Users/s1500174/Documents/data_01/data_01/diab_data.csv")

print(file_diab)

print(file_diab.info())

print(file_diab.describe())
