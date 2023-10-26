import mysql.connector
from mysql.connector import errorcode
import requests

from getInflation import (
    getRBAInflation,
    getExpantismSectorPrices,
    getExpantismMonthlyCost,
    getColesApples,
    getColesChicken,
    getColesBread,
    getColesBananas,
)
from getInflation import (
    getWooliesBread,
    getWooliesApples,
    getWooliesBananas,
    getWooliesChicken,
)
from getInflation import getAIPFuel, getCoreLogic, getAlcoholDaniels, getAlcoholAsahi


def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host="inflationdb.mysql.database.azure.com",
            username="Oakmont",
            password="StrattonStonks741",
            database="oakmont_padb",
        )
        print("Connection established\n")
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your credentials.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")


def update_db(name, sku, description, brand_name, url, expenditure_class, price):
    try:
        cursor = connection.cursor()
        
        # Check if product already exists in the database
        select_product = """
        SELECT productID
        FROM products 
        WHERE names = %s AND description = %s AND url = %s
        """
        cursor.execute(select_product, (name, description, url))
        existing_product = cursor.fetchone()

        # If product does not exist, insert it into the products table
        if not existing_product:
            insert_product = """
            INSERT INTO products (names, sku, description, brand_name, url, expenditure_class) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(
                insert_product, (name, sku, description, brand_name, url, expenditure_class)
            )
            connection.commit()
            product_id = cursor.lastrowid
        else:
            product_id = existing_product[0]
            print(f"Product with name '{name}' and description '{description}' and URL '{url}' already exists with ID {product_id}. Not inserting again.")

        # Insert price into the prices table
        insert_price = "INSERT INTO prices (productID, price) VALUES (%s, %s)"
        cursor.execute(insert_price, (product_id, price))
        connection.commit()

        print("Data successfully inserted into the database.")
    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()



# Call the functions and print the results
if __name__ == "__main__":
    try:
        print(":::Scraping Beginning:::\n")

        connection = create_db_connection()

        print("Getting RBA inflation data...")
        CPI, MPI = getRBAInflation()
        url = "https://www.rba.gov.au/inflation-overview.html"
        print(f"Consumer Price Index: {CPI}")
        print(f"Monthly Price Index: {MPI}")

        print("\nGetting sector prices from expatistan...")
        url = "https://www.expatistan.com/cost-of-living/country/australia"
        sector_prices = getExpantismSectorPrices()
        for item in sector_prices:
            name = item[0]
            price = item[1]
            url = url

            print(f"Item: {item[0]}, Price: {item[1]}")

        print("\nGetting monthly cost from expatistan...")
        url = "https://www.expatistan.com/cost-of-living/country/australia"
        monthly_cost = getExpantismMonthlyCost()
        print(f"Monthly Cost: {monthly_cost}")

        print("\nGetting Coles apples price...")
        apples_price, apples_url = getColesApples()
        name = "Apples"
        sku = ""
        description = apples_price[1]
        brand_name = "Coles"
        url = apples_url
        expenditure_class = "Fruit"

        price = apples_price[0]

        update_db(name, sku, description, brand_name, url, expenditure_class, price)

        print(
            f"Coles Apples Price: {apples_price[0]}, Weight: {apples_price[1]}, URL: {apples_url}"
        )

        print("\nGetting Coles bread price...")
        bread_price, bread_url = getColesBread()
        name = "Bread"
        sku = ""
        description = bread_price[1]
        brand_name = "Coles"
        url = bread_url
        expenditure_class = "Bread"

        price = bread_price[0]

        update_db(name, sku, description, brand_name, url, expenditure_class, price)

        print(
            f"Coles Bread Price: {bread_price[0]}, Weight: {bread_price[1]}, URL: {bread_url}"
        )

        print("\nGetting Coles bananas price...")
        bananas_price, bananas_url = getColesBananas()
        name = "Bananas"
        sku = ""
        description = bananas_price[1]
        brand_name = "Coles"
        url = bananas_url
        expenditure_class = "Fruit"

        price = bananas_price[0]

        update_db(name, sku, description, brand_name, url, expenditure_class, price)

        print(
            f"Coles Bananas Price: {bananas_price[0]}, Weight: {bananas_price[1]}, URL: {bananas_url}"
        )

        print("\nGetting Coles chicken price...")
        chicken_price, chicken_url = getColesChicken()
        name = "Chicken"
        sku = ""
        description = chicken_price[1]
        brand_name = "Coles"
        url = chicken_url
        expenditure_class = "Poultry"

        price = chicken_price[0]

        update_db(name, sku, description, brand_name, url, expenditure_class, price)

        print(
            f"Coles Chicken Price: {chicken_price[0]}, Weight: {chicken_price[1]}, URL: {chicken_url}"
        )

        print("\nGetting Woolies bread price...")
        woolies_bread_price, woolies_bread_url = getWooliesBread()
        name = "Bread"
        sku = ""
        description = woolies_bread_price[1]
        brand_name = "Woolworths"
        url = woolies_bread_url
        expenditure_class = "Bread"

        price = woolies_bread_price[0]

        update_db(name, sku, description, brand_name, url, expenditure_class, price)

        print(
            f"Woolies Bread Price: {woolies_bread_price[0]}, Weight: {woolies_bread_price[1]}, URL: {woolies_bread_url}"
        )

        print("\nGetting Woolies apples price...")
        woolies_apples_price, woolies_apples_url = getWooliesApples()
        name = "Apples"
        sku = ""
        description = woolies_apples_price[1]
        brand_name = "Woolworths"
        url = woolies_apples_url
        expenditure_class = "Fruit"

        price = woolies_apples_price[0]

        update_db(name, sku, description, brand_name, url, expenditure_class, price)

        print(
            f"Woolies Apples Price: {woolies_apples_price[0]}, Weight: {woolies_apples_price[1]}, URL: {woolies_apples_url}"
        )

        print("\nGetting Woolies bananas price...")
        woolies_bananas_price, woolies_bananas_url = getWooliesBananas()
        name = "Bananas"
        sku = ""
        description = woolies_bananas_price[1]
        brand_name = "Woolworths"
        url = woolies_bananas_url
        expenditure_class = "Fruit"

        price = woolies_bananas_price[0]

        update_db(name, sku, description, brand_name, url, expenditure_class, price)

        print(
            f"Woolies Bananas Price: {woolies_bananas_price[0]}, Weight: {woolies_bananas_price[1]}, URL: {woolies_bananas_url}"
        )
        """
        print("\nGetting Woolies chicken price...")
        woolies_chicken_price, woolies_chicken_url = getWooliesChicken()
        name = "Chicken"
        sku = ""
        description = woolies_chicken_price[1]
        brand_name = "Woolworths"
        url = woolies_chicken_url
        expenditure_class = "Poultry"

        price = woolies_chicken_price[0]

        update_db(name, sku, description, brand_name, url, expenditure_class, price)

        print(
            f"Woolies Chicken Price: {woolies_chicken_price[0]}, Weight: {woolies_chicken_price[1]}, URL: {woolies_chicken_url}"
        )
        """
        print("\nGetting AIP fuel price...")
        url = "http://www.aip.com.au/pricing/national-retail-petrol-prices"
        aip_fuel_price = getAIPFuel()
        name = "Fuel"
        sku = ""
        description = "AIP Fuel Price"
        brand_name = "AIP"
        url = url
        expenditure_class = "Automotive fuel"

        price = aip_fuel_price

        update_db(name, sku, description, brand_name, url, expenditure_class, price)

        print(f"AIP Fuel Price: {aip_fuel_price}")

        print("\nGetting CoreLogic housing prices...")
        url = "https://www.corelogic.com.au/our-data/corelogic-indices"
        corelogic_prices = getCoreLogic()
        for item in corelogic_prices:
            name = f"{item[0]} Housing Price"
            sku = ""
            description = "Housing Price"
            brand_name = "CoreLogic"
            url = url
            expenditure_class = "New dwelling purchase by owner-occupiers"

            price = item[1]

            update_db(name, sku, description, brand_name, url, expenditure_class, price)

            print(f"Location: {item[0]}, Price Index: {item[1]}")

        print("\nGetting Jack Daniels price...")
        url = "https://www.mybottleshop.au/jack-daniels-1907-white-label-heritage-bottle-700ml"
        jack_daniels_price = getAlcoholDaniels()
        name = "Jack Daniels"
        sku = ""
        description = "Jack Daniels Alcohol Price"
        brand_name = "mybottleshop.au"
        url = url
        expenditure_class = "Spirits"

        price = jack_daniels_price

        update_db(name, sku, description, brand_name, url, expenditure_class, price)

        print(f"Jack Daniels Price: {jack_daniels_price}")

        print("\nGetting Asahi price...")
        url = (
            "https://www.mybottleshop.au/asahi-super-dry-black-bottle-18x334ml-bottles"
        )
        asahi_price = getAlcoholAsahi()
        name = "Asahi"
        sku = ""
        description = "Asahi Alcohol Price"
        brand_name = "mybottleshop.au"
        url = url
        expenditure_class = "Beer"

        price = asahi_price

        update_db(name, sku, description, brand_name, url, expenditure_class, price)

        print(f"Asahi Price: {asahi_price}")

        print("\n:::Scraping Complete:::\n")

        print(":::Calculating Inflation:::\n")
        import inflationCalc

        final_estimation = inflationCalc.return_inflation()
        print(f"Final Estimation: {final_estimation}")
        final_estimation = final_estimation.replace("%", "").strip()
        try:
            cursor = connection.cursor()
            insert_result = "INSERT INTO results (inflation_prediction) VALUES (%s)"
            cursor.execute(insert_result, (final_estimation,))
            connection.commit()
            print("Inflation calculated and inserted into the database.")
        except mysql.connector.Error as err:
            print(f"MySQL error: {err}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()

        connection.close()
    except Exception as e:
        print(f"An error occurred: {e}")
