# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:15:39 2019

@author: Lab-C
"""

import operator
import os
import pandas
import matplotlib.pyplot as mpl
import numpy

# monthly_sales.py

#Pulling Data from CSV File Using Pandas

month_input = input("Please input a month for sales data (01 for January, 12 for December):")
year_input = input("Please input a 4-digit year for sales data:")


#IF Statement to Correctly Restart Program for an incorrect value
try:
    csv_location = "sales-" + year_input + month_input + ".csv"

    csv_found = os.path.join(os.path.dirname(__file__), "data", csv_location)  

    csv_data = pandas.read_csv(csv_found)
    print(csv_data)
    
except FileNotFoundError:
    print("the file does not exist")