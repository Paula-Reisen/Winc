import csv


def Inventory(Products, Quantity, buyprice, experation_Date):
    listproducts = []
    with open('Product_Amount.csv', newline='') as csvfile:
        csvdata = csv.DictReader(csvfile)
        for row in csvdata:
            listproducts.append(row['Product Name'])
            listproducts.append(row['Quantity'])
            listproducts.append(row['Buy Price'])
            listproducts.append(row['Expiration Date'])
        return(listproducts)


def AddProductAndAmountToInventory(Products, Quantity, buyprice, experation_Date):
    listproducts = Inventory(Products, Quantity, buyprice, experation_Date)
    if Products not in listproducts:
        listproducts.append(Products)
        listproducts.append(Quantity)
        listproducts.append(buyprice)
        listproducts.append(experation_Date)
    print(listproducts)
