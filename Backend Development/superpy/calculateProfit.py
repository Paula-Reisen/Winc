# Imports
from handle_date import handle_date
import os
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'


def calculate_profit(input_date):
    # Do a check if input date is of the YYYY-MM-DD format
    if handle_date(input_date) == False:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        return
    elif handle_date(input_date) == True:
        input_date = pd.to_datetime(input_date)
    # check if anything was sold
    if os.path.isfile("sold.csv") == False:
        print("There is nothing sold yet")
    if os.path.isfile("bought.csv") == False:
        print("There is nothing bought yet")
    elif os.path.isfile("sold.csv") & os.path.isfile("bought.csv"):
        sold = pd.read_csv("sold.csv")
        bought = pd.read_csv("bought.csv")

        # check which items are bought before or at this input date
        bought["Buy_date"] = pd.to_datetime(bought["Buy_date"])
        bought["Bought"] = input_date >= bought["Buy_date"]
        bought_true = bought[bought["Bought"] == True]

        # check which items are sold before or at this input date
        sold["Sell_date"] = pd.to_datetime(sold["Sell_date"])
        sold["Sold"] = input_date >= sold["Sell_date"]
        sold_true = sold[sold["Sold"] == True]

        # calculate costs of bought products
        bought_true["Buy_price"] = pd.to_numeric(
            bought_true["Buy_price"])
        bought_true["Quantity"] = pd.to_numeric(bought_true["Quantity"])
        bought_true["Costs"] = (
            bought_true["Quantity"] * bought_true["Buy_price"]
        )

        # calculate benefits of sold products
        sold_true["Sell_price"] = pd.to_numeric(sold_true["Sell_price"])
        sold_true["Quantity"] = pd.to_numeric(sold_true["Quantity"])
        sold_true["Benefit"] = sold_true["Quantity"] * \
            sold_true["Sell_price"]

        # calculate profit
        total_costs = bought_true["Costs"].sum()
        total_benefit = sold_true["Benefit"].sum()
        total_profit = total_benefit - total_costs
        date = input_date.strftime("%Y-%m-%d")

        if int(total_benefit) == 0:
            print("No products sold before or on:" + " " + date)
        if int(total_costs) == 0:
            print("No products bought before or on:" + " " + date)
        else:
            print("Products bought before or on:" + " " + date)
            print(bought_true)
            print("Products sold before or on:" + " " + date)
            print(sold_true)
            print("Total costs:" + str(total_costs))
            print("Total benefit:" + str(total_benefit))
            print("Total profit:" + str(total_profit))
