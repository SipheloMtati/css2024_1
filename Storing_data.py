# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:43:02 2024

@author: s1500174
"""

# Storing Data
B1 = 30	
B2 = 40
B3 = 30
B4 = 49

print(B1)
print(B2)

# Using Lists
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

# Lists indexes start at 0 which has the value of 30
print(age[0])
print(age[1])
print(age[10])

# This will give an error as there is no value at index 11
print(age[11])

# Basic Stats
age = [30,40,30,49,22,35,22,46,29,25,39]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

#Storing texts
C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
print(C3)
print(C4)

#Gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])
# [-1] to print the last observation

#we can do the same for name of countries

country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(country)
print(country[0])
print(country[5])

#LISTS
# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)
print(my_list[:])

my_list.append("pi")
print(my_list)

# INSERT pi2 in index/position 1
my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)

#length of my_list
print(len(my_list))

# View a certain range of items:
print(my_list[0:3])