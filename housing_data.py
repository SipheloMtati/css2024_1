# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:26:17 2024

@author: s1500174
"""

import pandas

file_housing = pandas.read_csv("C:/Users/s1500174/Documents/data_01/data_01/housing_data.csv", header = None)

print(file_housing)

print(file_housing.info())

print(file_housing.describe())

file_housing.columns = ["A" , "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
print(file_housing)