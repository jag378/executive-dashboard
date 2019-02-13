# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:37:42 2019

@author: jag378
"""

import operator
import os
import pandas
import matplotlib.pyplot as mpl
import numpy

# monthly_sales.py

#Pulling Data from CSV File Using Pandas

csv_location = "sales-201803.csv"

csv_location = os.path.join(os.path.dirname(__file__), "data", csv_location)

csv_data = pandas.read_csv(csv_location)


#Calculating Sales Data

#Converting Price to Dollar Format
def price_dollar(price):
    return "${0:,.2f}".format(price)

monthly_sales_total = csv_data["sales price"].sum()
print("TOTAL MONTHLY SALES: " + str(price_dollar(monthly_sales_total)))

by_product = csv_data.groupby(["product"]).sum()

#Sort the Products Highest to Lowest

by_product_sorted = by_product.sort_values("sales price",ascending=False)

print("\n")

#Found code to add rankings to specific rows from source: https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas

ranking = 1
best_sellers = []


for index, row in by_product_sorted.iterrows():
    #could not find how to print name of product, so referred to Prof. Rossetti's code for the row.name formula
    sales_dict = {"Rank": ranking, "Name": row.name, "Sales": row["sales price"]}
    best_sellers.append(sales_dict)
    ranking = ranking + 1

print("THIS MONTH'S TOP SELLERS:")
headers = list(best_sellers)
for row in best_sellers:
    print(str(row["Rank"]) + ". " + str(row["Name"]) + " " + price_dollar(row["Sales"]))


#Printing the Bar Graph

bar_chart = pandas.DataFrame(best_sellers)
test = bar_chart.plot.bar(x="Name", y="Sales")

#Sizing and Format
mpl.title("Monthly Sales by Product")
mpl.xlabel("Product Name")
mpl.ylabel("$ Sales")


mpl.show()


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