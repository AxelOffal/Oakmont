from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import errorcode
import plotly
import plotly.graph_objs as go
import json

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
template_path = os.path.join(dir_path, "..", "templates")
static_path = os.path.join(dir_path, "..", "static")

app = Flask(__name__, template_folder=template_path, static_folder=static_path)


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


def get_most_recent_prediction():
    # Establish database connection
    connection = create_db_connection()
    if not connection:
        return None

    # Create a cursor to execute the query
    cursor = connection.cursor()

    # Execute the query to get the most recent prediction based on the timestamp
    query = """
    SELECT prediction_timestamp, inflation_prediction 
    FROM results 
    ORDER BY prediction_timestamp DESC 
    LIMIT 1;
    """
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()
    data = None
    if result:
        data = {
            "timestamp": result[0].strftime("%Y-%m-%d %H:%M:%S"),
            "prediction": result[1],
        }

    cursor.close()
    connection.close()

    return data


def get_most_recent_abs_inflation():
    # Establish database connection
    connection = create_db_connection()
    if not connection:
        return None

    # Create a cursor to execute the query
    cursor = connection.cursor()

    # Execute the query to get the most recent entry based on the date
    query = """
    SELECT date, value 
    FROM abs_inflation 
    ORDER BY date DESC 
    LIMIT 1;
    """
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()
    data = None
    if result:
        data = {"date": result[0].strftime("%Y-%m-%d"), "value": result[1]}

    cursor.close()
    connection.close()

    return data


def get_trend_data():
    # Establish database connection
    connection = create_db_connection()
    if not connection:
        return None

    # Create a cursor to execute the query
    cursor = connection.cursor()

    # Execute the query to get all results from the results table
    query = """
    SELECT prediction_timestamp, inflation_prediction 
    FROM results 
    ORDER BY prediction_timestamp ASC;
    """
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    dates = [row[0] for row in results]
    predictions = [row[1] for row in results]

    cursor.close()
    connection.close()

    return dates, predictions


def get_data_for_month(year, month):
    # Establish database connection
    connection = create_db_connection()
    if not connection:
        return None

    # Create a cursor to execute the query
    cursor = connection.cursor()

    # Execute the query to get all results from the results table for the specified month
    query = """
    SELECT prediction_timestamp, inflation_prediction 
    FROM results 
    WHERE YEAR(prediction_timestamp) = %s AND MONTH(prediction_timestamp) = %s
    ORDER BY prediction_timestamp ASC;
    """
    cursor.execute(query, (year, month))

    # Fetch all the results
    results = cursor.fetchall()

    dates = [row[0] for row in results]
    predictions = [row[1] for row in results]

    cursor.close()
    connection.close()

    return dates, predictions


def get_available_months():
    # Establish database connection
    connection = create_db_connection()
    if not connection:
        return []

    # Create a cursor to execute the query
    cursor = connection.cursor()

    # Execute the query to get distinct months and years from results table
    query = """
    SELECT DISTINCT YEAR(prediction_timestamp), MONTH(prediction_timestamp)
    FROM results 
    ORDER BY YEAR(prediction_timestamp) DESC, MONTH(prediction_timestamp) DESC;
    """
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Format results to "YYYY-MM" format
    formatted_dates = [f"{row[0]}-{str(row[1]).zfill(2)}" for row in results]

    cursor.close()
    connection.close()

    return formatted_dates


@app.route("/")
def index():
    view = request.args.get("view", "all")
    month = request.args.get("month", None)  # Get the month parameter

    if view == "all":
        dates, predictions = get_trend_data()
    elif view == "month" and month:  # Make sure month is provided
        year, month = month.split("-")
        dates, predictions = get_data_for_month(int(year), int(month))
    else:  # Default to all if no valid view or month is provided
        dates, predictions = get_trend_data()

    # Get the most recent prediction
    data = get_most_recent_prediction()
    if not data:
        data = {"timestamp": "N/A", "prediction": "N/A"}

    # Get the most recent abs_inflation data
    abs_inflation_data = get_most_recent_abs_inflation()
    if not abs_inflation_data:
        abs_inflation_data = {"date": "N/A", "value": "N/A"}

    # Get available months
    available_months = get_available_months()

    # Create graph
    graph = {
        "data": [
            go.Scatter(x=dates, y=predictions, mode="lines+markers", name="Predictions")
        ],
        "layout": {
            "title": "Inflation Predictions Over Time",
            "xaxis": {
                "title": "Date",
                "titlefont": dict(family="Times New Roman, Times, serif"),
                "tickfont": dict(family="Times New Roman, Times, serif"),
            },
            "yaxis": {
                "title": "Inflation Prediction",
                "titlefont": dict(family="Times New Roman, Times, serif"),
                "tickfont": dict(family="Times New Roman, Times, serif"),
            },
            "font": dict(family="Times New Roman, Times, serif"),
            "plot_bgcolor": "#f7f7f7",
            "paper_bgcolor": "#f7f7f7",
            "margin": {"t": 60, "b": 60, "l": 50, "r": 10},
        },
    }

    graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template(
        "index.html",
        timestamp=data["timestamp"],
        prediction=data["prediction"],
        graphJSON=graphJSON,
        abs_date=abs_inflation_data["date"],
        abs_value=abs_inflation_data["value"],
        available_months=available_months,  # Pass the months to the template
    )


if __name__ == "__main__":
    app.run()
