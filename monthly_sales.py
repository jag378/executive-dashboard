# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:37:42 2019

@author: jag378
"""

import operator
import os
import pandas
import matplotlib.pyplot as mpl


# monthly_sales.py

#Pulling Data from CSV File Using Pandas

csv_location = "sales-201803.csv" # TODO: allow user to specify

csv_location = os.path.join(os.path.dirname(__file__), "data", csv_location)

csv_data = pandas.read_csv(csv_location)

print(csv_data)

#Calculating Sales Data

monthly_sales_total = csv_data["sales price"].sum()
print(monthly_sales_total)

by_product = csv_data.groupby(["product"]).sum()
print(by_product)

#Sort the Products Highest to Lowest
by_product_sorted = by_product.sort_values("sales price",ascending=False)
print(by_product_sorted)


print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")