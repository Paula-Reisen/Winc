from handle_date import handle_date
from record_sell import record_sell
import os
import pandas as pd
import datetime

pd.options.mode.chained_assignment = None  # default='warn'


def add_sell_to_inventory(product, price, sell_date, quantity):
    # check if sell_date is filled otherwise get the time from advanced or fill in the current date of today
    if sell_date == None:
        if os.path.isfile("advanced_date_save.csv") == False:
            today = datetime.datetime.now()
            sell_date = today.date()
            sell_date = str(sell_date)
        else:
            Current_date = pd.read_csv("advanced_date_save.csv")
            print(Current_date)

            sell_date = pd.to_datetime(
                Current_date["date"].iloc[0], format="%Y-%m-%d").date()
            sell_date = str(sell_date)
            print(sell_date)
    # check if sell_date is of the YYYY-MM-DD format
    if handle_date(sell_date) == False:
        (print(+"This is the incorrect date string format. It should be YYYY-MM-DD"))
        return
    # check if inventory already exists
    if os.path.isfile("inventory.csv") == False:
        print("There is nothing in the current inventory")
    # check if item with Product_name is present in inventory and if quantity is enough
    elif os.path.isfile("inventory.csv"):
        Inventory = pd.read_csv("inventory.csv")
        Inventory["Quantity"] = pd.to_numeric(Inventory["Quantity"])
        product_exists = (
            (Inventory["Product_name"] == product)
            & (Inventory["Quantity"] >= quantity)
        ).any()
        if product_exists == False:
            print(product + " " + "is not (sufficiently) present in inventory")
        # if product is already present in inventory, get the product_index
        elif product_exists:
            product_index = Inventory[
                (
                    (Inventory["Product_name"] == product)
                    & (Inventory["Quantity"] >= quantity)
                )
            ].index.tolist()
            # start selling products that were added first
            product_index = product_index[0]
            # check if product is not expired
            if pd.to_datetime(
                Inventory["Expiration_date"].iloc[product_index], format="%Y-%m-%d"
            ) > pd.to_datetime(sell_date, format="%Y-%m-%d"):
                print("Product is already expired at this Sell date")
            # Quantity and Sell_date are OK, product is sold and quantity is updated
            else:
                id = Inventory["Product_ID"].iloc[product_index]
                record_sell(id, product, price, sell_date, quantity)
                new_quantity = int(Inventory["Quantity"].iloc[product_index]) - int(
                    quantity
                )
                # if all products are sold, complete row is deleted
                if new_quantity == 0:
                    Inventory = Inventory.drop(
                        Inventory.index[product_index])
                    print("Updated inventory:")
                    print(Inventory.to_string(index=False))
                    return Inventory.to_csv("inventory.csv", index=False)
                else:
                    # update quantity
                    Inventory["Quantity"].iloc[product_index] = new_quantity
                    print("Updated inventory:")
                    print(Inventory.to_string(index=False))
                    return Inventory.to_csv("inventory.csv", index=False)
