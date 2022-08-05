import pandas as pd

from handle_date import handle_date
from record_buy import record_buy
import os

pd.options.mode.chained_assignment = None  # default='warn'


def add_buy_to_inventory(id, product, price, quantity, buy_date, exp_date):
    # check if exp_date and buy_date are of the YYYY-MM-DD format
    if (handle_date(exp_date) == False) | (handle_date(buy_date) == False):
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        return
    # check if inventory already exists and if not create file
    if os.path.isfile("Inventory.csv") == False:
        Inventory = pd.DataFrame(
            columns=[
                "Product_ID",
                "Product_name",
                "Quantity",
                "Expiration_date",
            ]
        )
        # create new inventory item and append
        count_row = Inventory.shape[0]
        id = count_row + 1
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Quantity": quantity,
            "Expiration_date": exp_date,
        }
        Inventory = Inventory.append(new_row, ignore_index=True)
        print(product + " was added to inventory")
        print("Updated inventory:")
        print(Inventory.to_string(index=False))
        # add item to list of bought items
        record_buy(id, product, price, buy_date, quantity, exp_date)
        return Inventory.to_csv("df_inventory.csv", index=False)
    # if inventory already exists, search product with same Product_name, Expiration_date
    elif os.path.isfile("df_inventory.csv"):
        Inventory = pd.read_csv("df_inventory.csv")
        product_exists = (
            (Inventory["Product_name"] == product)
            & ((Inventory["Expiration_date"] == exp_date))
        ).any()
        # if product does not already exist, create and append new item
        if product_exists == False:
            count_row = Inventory.shape[0]
            id = count_row + 1
            new_row = {
                "Product_ID": id,
                "Product_name": product,
                "Quantity": quantity,
                "Expiration_date": exp_date,
            }
            Inventory = Inventory.append(new_row, ignore_index=True)
            print(product + " was added to inventory")
            print("Updated inventory:")
            print(Inventory.to_string(index=False))
            # add item to list of bought items
            record_buy(id, product, price, buy_date, quantity, exp_date)
            return Inventory.to_csv("df_inventory.csv", index=False)
        # if product already exists, get the product_index and update the Quantity
        elif product_exists:
            product_index = Inventory[
                (
                    (Inventory["Product_name"] == product)
                    & ((Inventory["Expiration_date"] == exp_date))
                )
            ].index.tolist()
            product_index = product_index[0]
            id = int(Inventory["Product_ID"].iloc[product_index])
            current_quantity = Inventory["Quantity"].iloc[product_index]
            new_quantity = int(current_quantity) + int(quantity)
            Inventory["Quantity"].iloc[product_index] = new_quantity
            print(
                product + " is already in inventory, quantity is updated to:",
                new_quantity,
            )
            print("Updated inventory:")
            print(Inventory.to_string(index=False))
            # add item to list of bought items
            record_buy(id, product, price, buy_date, quantity, exp_date)
            return Inventory.to_csv("Inventory.csv", index=False)
