import pandas
import os
from handle_date import handle_date


def export(selection, date):
    # check if input date is of the YYYY-MM-DD format
    if handle_date(date) == False:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        return
    elif handle_date(date) == True:
        date = pandas.to_datetime(date)
    if selection == "expired":
        if os.path.isfile("inventory.csv") == False:
            print("There is no data in the current inventory")
        # create new column comparing the input date to the Expiration_date
        elif os.path.isfile("inventory.csv"):
            inventory = pandas.read_csv("inventory.csv")
            inventory["Expiration_date"] = pandas.to_datetime(
                inventory["Expiration_date"], format="%Y-%m-%d"
            )
            inventory["Expired"] = inventory["Expiration_date"] < date
            # select Expired products only
            inventory_selection = inventory[inventory["Expired"] == True]
            if inventory_selection.empty:
                print("There are no expired products at this date")
            else:
                print("Expired products on selected date:")
                print(inventory_selection.to_string(index=False))
                print("Data is exported to Expired.csv")
                return inventory_selection.to_csv("Expired.csv", index=False)
    if selection == "bought":
        if os.path.isfile("bought.csv") == False:
            print("There is no data in the bought administration")
        elif os.path.isfile("inventory.csv"):
            bought = pandas.read_csv("bought.csv")
            bought["Buy_date"] = pandas.to_datetime(bought["Buy_date"])
            # create new column comparing the input date to the Buy_date
            bought["Bought"] = bought["Buy_date"] <= date
            # select Bought products only
            bought_selection = bought[bought["Bought"] == True]
            if bought_selection.empty:
                print("No bought products before or on this date")
            else:
                print("Bought products on selected date:")
                print(bought_selection.to_string(index=False))
                print("Data is exported to Bought.csv")
                return bought_selection.to_csv("Bought.csv", index=False)
    if selection == "sold":
        if os.path.isfile("sold.csv") == False:
            print("There is no data in the sold administration")
        elif os.path.isfile("sold.csv"):
            sold = pandas.read_csv("sold.csv")
            sold["Sell_date"] = pandas.to_datetime(sold["Sell_date"])
            # create new column comparing the input date to the Sell_date
            sold["Sold"] = sold["Sell_date"] <= date
            # select Sold products only
            sold_selection = sold[sold["Sold"] == True]
            if sold_selection.empty:
                print("No sold products before or on this date")
            else:
                print("Sold products on selected date:")
                print(sold_selection.to_string(index=False))
                print("Data is exported to Sold.csv")
                return sold_selection.to_csv("Bought.csv", index=False)
