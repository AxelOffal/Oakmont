# -*- coding: utf-8 -*-
import mysql.connector
from datetime import datetime, timedelta
from decimal import Decimal


class Database:
    def __init__(self, user, password, host, database):
        self.connection = mysql.connector.connect(user=user, password=password, host=host, database=database)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

def fetch_unique_classes(db):
    query = "SELECT DISTINCT expenditure_class FROM products"
    return db.execute_query(query)


def fetch_product_data(db, e_class):
    query = "SELECT productID, names FROM products WHERE expenditure_class = %s"
    return db.execute_query(query, (e_class,))


def fetch_prices(db, productID, month, year):
    # This query fetches the first and last prices for a given product in a specified month and year
    query = """
    SELECT price, timestamp
    FROM prices
    WHERE productID = %s
    AND MONTH(timestamp) = %s AND YEAR(timestamp) = %s
    ORDER BY timestamp ASC
    """

    results = db.execute_query(query, (productID, month, year))
    # If no results are found, return None
    if not results:
        return None

    # If there's only one result, then it's both the first and last price
    if len(results) == 1:
        return None

    # If there's more than one result, then the first is the earliest and the last is the latest price
    first_price, first_price_time = results[0]
    last_price, last_price_time = results[-1]

    return (first_price, first_price_time), (last_price, last_price_time)


def fetch_class_weights(db, class_inflation_list):
    class_weights = []
    for e_class, _ in class_inflation_list:
        query = "SELECT weights FROM abs_weights WHERE expenditure_class = %s"
        weight = db.execute_query(query, (e_class,))
        if weight:
            class_weights.append((e_class, weight[0][0]))
    return class_weights

def rescale_weights(class_weights):
    # Calculate the total sum of the weights
    total_weight = sum(weight for _, weight in class_weights)
    # Rescale the weights so they add up to 1
    rescaled_weights = [(e_class, (weight / total_weight)) for e_class, weight in class_weights]
    return rescaled_weights

def calculate_weighted_inflation(class_inflation_list, rescaled_weights):
    weighted_inflations = []
    for e_class, avg_inflation in class_inflation_list:
        for class_with_weight, rescaled_weight in rescaled_weights:
            if e_class == class_with_weight:
                weighted_inflation = float(avg_inflation) * rescaled_weight
                weighted_inflations.append((e_class, weighted_inflation))
                print(f"Class: {e_class}, Weighted Inflation: {weighted_inflation:.4f}")
    return weighted_inflations

def fetch_cpi_data(db):
    query_latest_cpi = "SELECT date, value FROM abs_inflation ORDER BY date DESC LIMIT 1"
    latest_cpi_date, latest_cpi_value = db.execute_query(query_latest_cpi)[0]

    query_past_cpi = f"SELECT date, value FROM abs_inflation WHERE date = '{latest_cpi_date}' - INTERVAL 11 MONTH"
    past_cpi_date, past_cpi_value = db.execute_query(query_past_cpi)[0]
    
    return (latest_cpi_date, latest_cpi_value, past_cpi_date, past_cpi_value)

def process_class(db, e_class, month, year):
    print(f"Processing products of class: {e_class}")

    inflation_sum = 0
    product_count = 0

    products = fetch_product_data(db, e_class)

    for productID, names in products:
        
        result = fetch_prices(db, productID, month, year)
        if not result:
            print(f"No valid price data found for product {productID} ({names}).")
            continue
        # Unpack the results into separate variables
        (past_price, past_price_time), (latest_price, latest_price_time) = result
        days_difference = (latest_price_time - past_price_time).days
        months_difference = days_difference/Decimal(30.0)
        if months_difference == 0:
            print(f"No valid price data found for product {productID} ({names}).")
            continue
        if past_price != 0:
            inflation = ((latest_price - past_price) / past_price)/ months_difference
            print(f"Inflation for product {productID} ({names}): (({latest_price} - {past_price}) / {past_price}) {months_difference:.2f} = {inflation * 100:.2f}%")
            inflation_sum += inflation
            product_count += 1
        else:
            print("Past price is zero, cannot calculate inflation.")

    avg_inflation = 0
    if product_count > 0:
        avg_inflation = inflation_sum / product_count
        print(f"Average inflation for class {e_class}: {avg_inflation * 100:.2f}%")
    else:
        print(f"No valid inflation data available for class {e_class}.")

    return (e_class, avg_inflation)


def main():
    db = Database(user="Oakmont", password="StrattonStonks741", host="inflationdb.mysql.database.azure.com", database="oakmont_padb")
    
    latest_cpi_date, latest_cpi_value, past_cpi_date, past_cpi_value = fetch_cpi_data(db)
    #current_date = datetime.strptime(latest_cpi_date, '%Y-%m-%d %H:%M:%S')
    current_month = latest_cpi_date.month + 1 
    current_year = latest_cpi_date.year
    all_classes = fetch_unique_classes(db)
    # Iterate through classes and process data
    class_inflation_list = []
    for e_class in all_classes:
        class_inflation = process_class(db, e_class[0], current_month, current_year)
        if class_inflation[1] !=0:
            class_inflation_list.append(class_inflation)
            
    class_weights = fetch_class_weights(db, class_inflation_list)
    
    rescaled_weights = rescale_weights(class_weights)
    
    weighted_inflations = calculate_weighted_inflation(class_inflation_list, rescaled_weights)
    
    overall_inflation = sum(inflation for _, inflation in weighted_inflations)
    print(f"Overall Inflation: {overall_inflation:.6f}")
    
    

    # Now you can use these variables in your main function
    print(f"Latest CPI value: {latest_cpi_value} at {latest_cpi_date}")
    print(f"CPI value from 11 months ago: {past_cpi_value} at {past_cpi_date}")

    # Continue with the rest of your main function
    if past_cpi_value != 0:  # Add a check to avoid division by zero
        cpi_inflation = (latest_cpi_value - past_cpi_value) / past_cpi_value
        print(f"CPI Inflation over the past 11 months: {cpi_inflation * 100:.2f}%")
    else:
        print("Past CPI value is zero, cannot calculate inflation.")
    final_inflation = cpi_inflation + (overall_inflation)
    returnsInflationFinal = (f"{final_inflation*100:.5F}%")
    db.close()
    return returnsInflationFinal

def return_inflation():
    return main()


