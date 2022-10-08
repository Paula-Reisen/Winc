# Imports
import pandas
import os


def record_sell(id, product, price, sell_date, quantity):
    # check if record of sold items already exists and if not create file
    if os.path.isfile("sold.csv") == False:

        sold = pandas.DataFrame(
            columns=[
                "Product_ID",
                "Product_name",
                "Sell_price",
                "Sell_date",
                "Quantity",
            ]
        )
        # create new item and append
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Sell_price": price,
            "Sell_date": sell_date,
            "Quantity": quantity,
        }

        sold = sold.append(new_row, ignore_index=True)
        print(product + " was added to SELL administration")
        return sold.to_csv("sold.csv", index=False)
    elif os.path.isfile("sold.csv"):

        sold = pandas.read_csv("sold.csv")
        # create new item and append to existing file
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Sell_price": price,
            "Sell_date": sell_date,
            "Quantity": quantity,
        }

        sold = sold.append(new_row, ignore_index=True)
        print(product + " was added to SELL administration")
        return sold.to_csv("sold.csv", index=False)
