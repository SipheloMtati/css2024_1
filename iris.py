# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:48:46 2024

@author: s1500174
"""
import pandas

file_iris = pandas.read_csv("C:/Users/s1500174/Documents/data_01/data_01/iris.csv")

print(file_iris)

print(file_iris.info())

print(file_iris.describe())