import pandas
import os


def record_buy(id, product, price, buy_date, quantity, exp_date):
    # check if record of bought items already exists and if not create file
    if os.path.isfile("df_bought.csv") == False:
        Bought = pandas.DataFrame(
            columns=[
                "Product_ID",
                "Product_name",
                "Buy_price",
                "Buy_date",
                "Quantity",
                "Expiration_date",
            ]
        )
        # create new item and append
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Buy_price": price,
            "Buy_date": buy_date,
            "Quantity": quantity,
            "Expiration_date": exp_date,
        }
        Bought = Bought.append(new_row, ignore_index=True)
        print(product + " was added to BUY administration")
        return Bought.to_csv("Bought.csv", index=False)
    elif os.path.isfile("Bought.csv"):
        Bought = pandas.read_csv("Bought.csv")
        # create new item and append to existing file
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Buy_price": price,
            "Buy_date": buy_date,
            "Quantity": quantity,
            "Expiration_date": exp_date,
        }
        Bought = Bought.append(new_row, ignore_index=True)
        print(product + " was added to to BUY administration")
        return Bought.to_csv("Bought.csv", index=False)
