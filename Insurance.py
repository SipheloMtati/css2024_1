# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:52:49 2024

@author: s1500174
"""

import pandas

file_insurance = pandas.read_csv("C:/Users/s1500174/Documents/data_01/data_01/insurance_data.csv", skiprows = 5)

print(file_insurance)

print(file_insurance.info())

print(file_insurance.describe())