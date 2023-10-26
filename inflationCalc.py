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
    """
    returns all the uniques classes in products

    """
    query = "SELECT DISTINCT expenditure_class FROM products"
    return db.execute_query(query)


def fetch_product_data(db, e_class):
    query = "SELECT productID, names FROM products WHERE expenditure_class = %s"
    return db.execute_query(query, (e_class,))


def fetch_prices(db, productID, month, year):
    """
    This function fetches the first and last prices and their timestamps for a 
    given product in a specified month and year
    """
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

    # If there's only one result, then we can't calculate inflation for that month
    if len(results) == 1:
        return None

    # If there's more than one result, then the first is the earliest and the last is the latest price
    first_price, first_price_time = results[0]
    last_price, last_price_time = results[-1]

    return (first_price, first_price_time), (last_price, last_price_time)


def fetch_class_weights(db, class_inflation_list):
    """
    Gets the abs weights for the weights in class_inflation_list
    """
    class_weights = []
    for e_class, _ in class_inflation_list:
        query = "SELECT weights FROM abs_weights WHERE expenditure_class = %s"
        weight = db.execute_query(query, (e_class,))
        if weight:
            class_weights.append((e_class, weight[0][0]))
    return class_weights


def rescale_weights(class_weights):
    """
    If we aren't calulating inflation for every class the abs uses we can't use the
    same weights unadjusted.
    This function rescales them so that the ABS weights can still be used, wihtout 
    scaling the inflation down
    """
    # Calculate the total sum of the weights used
    total_weight = sum(weight for _, weight in class_weights)
    # Rescale the weights so they add up to 1
    rescaled_weights = [(e_class, (weight / total_weight)) for e_class, weight in class_weights]
    return rescaled_weights


def calculate_weighted_inflation(class_inflation_list, rescaled_weights):
    """
    Multiplys the inflation for each class with its rescaled weight
    """
    weighted_inflations = []
    for e_class, avg_inflation in class_inflation_list:
        for class_with_weight, rescaled_weight in rescaled_weights:
            if e_class == class_with_weight:
                weighted_inflation = float(avg_inflation) * rescaled_weight
                weighted_inflations.append((e_class, weighted_inflation))
                print(f"Class: {e_class}, Weighted Inflation: {weighted_inflation:.4f}")
    return weighted_inflations


def fetch_cpi_data(db):
    """
    Returns the most recent CPI values and date along with the CPI value from 
    11 months ago and its date
    """
    query_latest_cpi = "SELECT date, value FROM abs_inflation ORDER BY date DESC LIMIT 1"
    latest_cpi_date, latest_cpi_value = db.execute_query(query_latest_cpi)[0]

    query_past_cpi = f"SELECT date, value FROM abs_inflation WHERE date = '{latest_cpi_date}' - INTERVAL 11 MONTH"
    past_cpi_date, past_cpi_value = db.execute_query(query_past_cpi)[0]
    
    return (latest_cpi_date, latest_cpi_value, past_cpi_date, past_cpi_value)


def process_class(db, e_class, month, year):
    """
    Calulates the average inflation for a specified month and year for a particular
    expenditure class
    This figure is not weighted
    """
    print(f"Processing products of class: {e_class}")

    inflation_sum = 0
    product_count = 0

    products = fetch_product_data(db, e_class)
    #for each product in the expenditure class
    for productID, names in products:
        #fetch the the first and last prices in a specified month
        result = fetch_prices(db, productID, month, year)
        if not result:
            print(f"No valid price data found for product {productID} ({names}).")
            continue
        # Unpack the results into separate variables
        (past_price, past_price_time), (latest_price, latest_price_time) = result
        #calulate how many months apart the prices came from
        #for example if two prices are a 6 days apart this is 0.2 of a month
        days_difference = (latest_price_time - past_price_time).days
        months_difference = days_difference/Decimal(30.0)
        if months_difference == 0:
            print(f"No valid price data found for product {productID} ({names}).")
            continue
        if past_price != 0:
            #The formula for monthly inflation
            inflation = ((latest_price - past_price) / past_price)/ months_difference
            print(f"Inflation for product {productID} ({names}): (({latest_price} - {past_price}) / {past_price}) {months_difference:.2f} = {inflation * 100:.2f}%")
            inflation_sum += inflation
            product_count += 1
        else:
            print("Past price is zero, cannot calculate inflation.")

    avg_inflation = 0
    if product_count > 0:
        #take the average inflation of all the products in the class
        #Note: there may be better ways of including multiple products then an average
        avg_inflation = inflation_sum / product_count
        print(f"Average inflation for class {e_class}: {avg_inflation * 100:.2f}%")
    else:
        print(f"No valid inflation data available for class {e_class}.")

    return (e_class, avg_inflation)


def main():
    db = Database(user="Oakmont", password="StrattonStonks741", host="inflationdb.mysql.database.azure.com", database="oakmont_padb")
    #need these values now so we know what month to calculate for. Will also 
    #use them later
    latest_cpi_date, latest_cpi_value, past_cpi_date, past_cpi_value = fetch_cpi_data(db)
    current_month = latest_cpi_date.month + 1 
    current_year = latest_cpi_date.year
    
    all_classes = fetch_unique_classes(db)
    # Iterate through each class and calulate the average inflation for it
    # Apenned the class and its inflation to class_inflation_list
    class_inflation_list = []
    for e_class in all_classes:
        class_inflation = process_class(db, e_class[0], current_month, current_year)
        if class_inflation[1] !=0:
            class_inflation_list.append(class_inflation)
    #Find the class weights for all the classes we calculate an inflation for
    class_weights = fetch_class_weights(db, class_inflation_list)
    #rescale those weights
    rescaled_weights = rescale_weights(class_weights)
    #Calulate the weighted inflation for each class using the rescaled weights
    weighted_inflations = calculate_weighted_inflation(class_inflation_list, rescaled_weights)
    #sum the weighted inflations to return the total inflation prediction for one month
    overall_inflation = sum(inflation for _, inflation in weighted_inflations)
    print(f"Overall Inflation: {overall_inflation:.6f}")
    
    
    print(f"Latest CPI value: {latest_cpi_value} at {latest_cpi_date}")
    print(f"CPI value from 11 months ago: {past_cpi_value} at {past_cpi_date}")

    #Calulate the inflation the ABS reported over the previous 11 months
    if past_cpi_value != 0:  
        cpi_inflation = (latest_cpi_value - past_cpi_value) / past_cpi_value
        print(f"CPI Inflation over the past 11 months: {cpi_inflation * 100:.2f}%")
    else:
        print("Past CPI value is zero, cannot calculate inflation.")
    #Add the predicted month of inflation to the previous 11 to generate final prediction
    final_inflation = cpi_inflation + (overall_inflation)
    returnsInflationFinal = (f"{final_inflation*100:.5F}%")
    db.close()
    return returnsInflationFinal

def return_inflation():
    return main()


