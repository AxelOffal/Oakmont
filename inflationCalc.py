# -*- coding: utf-8 -*-
"""
Created on Tue Oct 3 21:21:50 2023

@author: willi
"""
import mysql.connector
from datetime import datetime, timedelta

cnx = mysql.connector.connect(user='Oakmont', password='StrattonStonks741',
                              host='inflationdb.mysql.database.azure.com',
                              database='oakmont_padb')

cursor = cnx.cursor()

# Getting all unique classes
query_classes = "SELECT DISTINCT expenditure_class FROM products"
cursor.execute(query_classes)
all_classes = cursor.fetchall()
cursor.close()  # Close the cursor after fetching the results

class_inflation_list = []  

# Iterate through each class
for e_class in all_classes:
    e_class = e_class[0]  
    print(f"Processing products of class: {e_class}")
    
    inflation_sum = 0
    product_count = 0
    
    cursor = cnx.cursor()  # Create a new cursor for this loop
    query_products = ("SELECT productID, names FROM products "
                      "WHERE expenditure_class = %s")
    cursor.execute(query_products, (e_class,))
    products = cursor.fetchall()
    cursor.close()  # Close the cursor after fetching the results
    
    for productID, names in products:
        cursor = cnx.cursor()  # Create a new cursor for this loop
        # Get the most recent price
        query_latest_price = ("SELECT price FROM prices "
                              "WHERE productID = %s "
                              "ORDER BY timestamp DESC LIMIT 1")
        cursor.execute(query_latest_price, (productID,))
        latest_price = cursor.fetchone()[0]

        # Get a past price
        query_past_price = ("SELECT price FROM prices "
                            "WHERE productID = %s "
                            "ORDER BY timestamp ASC LIMIT 1")
        cursor.execute(query_past_price, (productID,))
        past_price = cursor.fetchone()[0]
        cursor.close()  # Close the cursor after fetching the results

        # Calculate the inflation
        if past_price != 0:  # Add a check to avoid division by zero
            inflation = (latest_price - past_price) / past_price
            print(f"Inflation for product {productID} ({names}):({latest_price} - {past_price}) / {past_price} = {inflation * 100:.2f}%")
            inflation_sum += inflation
            product_count += 1
        else:
            print("Past price is zero, cannot calculate inflation.")
            
    if product_count > 0:
        avg_inflation = inflation_sum / product_count
        print(f"Average inflation for class {e_class}: {avg_inflation * 100:.2f}%")
        class_inflation_list.append((e_class, avg_inflation))  # Adding the class and avg inflation to the list
    else:
        print(f"No valid inflation data available for class {e_class}.")
for item in class_inflation_list:
    print(f"Class: {item[0]}, Average Inflation: {item[1] * 100:.2f}%")
    
# Retrieve the weights for the classes that we have data for
cursor = cnx.cursor()

# This list will store tuples containing the class and its corresponding weight
class_weights = []

for e_class, _ in class_inflation_list:
    query_weights = ("SELECT weights FROM abs_weights "
                     "WHERE expenditure_class = %s")
    cursor.execute(query_weights, (e_class,))
    weight = cursor.fetchone()
    
    if weight is not None:  # Check if weight is found for the class
        class_weights.append((e_class, weight[0]))

cursor.close()

# Calculate the total sum of the weights
total_weight = sum(weight for _, weight in class_weights)

# Rescale the weights so they add up to 1
rescaled_weights = [(e_class, weight / total_weight) for e_class, weight in class_weights]

# Print out the rescaled weights for verification
for e_class, weight in rescaled_weights:
    print(f"Class: {e_class}, Rescaled Weight: {weight:.4f}")

weighted_inflations = []

# Multiply each rescaled weight by the average inflation in each class
for (e_class, avg_inflation) in class_inflation_list:
    for (class_with_weight, rescaled_weight) in rescaled_weights:
        if e_class == class_with_weight:
            weighted_inflation = float(avg_inflation) * rescaled_weight
            weighted_inflations.append((e_class, weighted_inflation))
            print(f"Class: {e_class}, Weighted Inflation: {weighted_inflation:.4f}")

# Calculate the sum of weighted inflations to get the overall inflation
overall_inflation = sum(inflation for _, inflation in weighted_inflations)
print(f"Overall Inflation: {overall_inflation:.4f}")

# Create a cursor to execute queries
cursor = cnx.cursor()

# Getting the latest CPI value
query_latest_cpi = ("SELECT date, value FROM abs_inflation "
                    "ORDER BY date DESC LIMIT 1")
cursor.execute(query_latest_cpi)
latest_cpi_date, latest_cpi_value = cursor.fetchone()
print(f"Latest CPI value: {latest_cpi_value} at {latest_cpi_date}")

# Getting the CPI value from 11 months ago
query_past_cpi = (f"SELECT date, value FROM abs_inflation "
                  f"WHERE date = '{latest_cpi_date}' - INTERVAL 11 MONTH")
cursor.execute(query_past_cpi)
past_cpi_date, past_cpi_value = cursor.fetchone()
print(f"CPI value from 11 months ago: {past_cpi_value} at {past_cpi_date}")

# Calculate the inflation based on the CPI values
if past_cpi_value != 0:  # Add a check to avoid division by zero
    cpi_inflation = (latest_cpi_value - past_cpi_value) / past_cpi_value
    print(f"CPI Inflation over the past 11 months: {cpi_inflation * 100:.2f}%")
else:
    print("Past CPI value is zero, cannot calculate inflation.")
final_inflation = cpi_inflation + (overall_inflation*4)
cursor.close()
cnx.close()
