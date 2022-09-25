SuperPy guidelines:
positional arguments: {buy,sell,export,profit,plot,reset}

buy:                 Buy a product
sell:                 Sell a product
export:            Export selection of data on a specific date
profit:              Calculate profit on a specific date
plot:                Plot bar graph of products in inventory, bought or sold list
reset:               Reset selection of files or all files
Commands:
1. Buy usage: super.py buy [-h] --product PRODUCT --buy-price PRICE [--quantity QUANTITY] --buy-date BUY_DATE --exp-date EXP_DATE

arguments: -h, --help show this help message and exit --product PRODUCT product name --buy-price PRICE buy price per product --quantity QUANTITY quantity of product --buy-date BUY_DATE product buy date (format YYYY-MM-DD) --exp-date EXP_DATE product expiration date (format YYYY-MM-DD)

Examples: python super.py buy --product Apple --buy-price 5 --buy-date 2022-01-05 --exp-date 2022-03-04 python super.py buy --product Apple --buy-price 5 --quantity 10 --buy-date 2022-01-05 --exp-date 2022-03-04

**2. Sell: ** usage: super.py sell [-h] --product PRODUCT --sell-price PRICE [--quantity QUANTITY] --sell-date SELL_DATE

arguments: -h, --help show this help message and exit --product PRODUCT product name --sell-price PRICE sell price per product --quantity QUANTITY quantity of product --sell-date SELL_DATE product sell date (format YYYY-MM-DD)

Examples: python super.py sell --product Orange --sell-price 21 --sell-date 2025-10-01 python super.py sell --product Orange --sell-price 21 --quantity 3 --sell-date 2025-10-01

3. Export usage: super.py export [-h] --file {expired,bought,sold} --date DATE

arguments: -h, --help show this help message and exit --file {expired,bought,sold} Data to be exported to .csv file --date DATE Choose date of interest(format YYYY-MM-DD)

Examples: python super.py export --file expired --date 2023-10-03 python super.py export --file bought --date 2021-09-02

4. Profit usage: super.py profit [-h] --date DATE

arguments: -h, --help show this help message and exit --date DATE Choose date of interest(format YYYY-MM-DD)

Examples: python super.py profit --date 2030-10-03 python super.py profit --date 2020-03-14

5. Plot usage: super.py plot [-h] --file {bought,sold,inventory}

arguments: -h, --help show this help message and exit --file {bought,sold,inventory} File to be plotted

Examples: python super.py plot --file inventory python super.py plot --file bought

6. Reset usage: super.py reset [-h] [--file {bought,sold,inventory,all}]

arguments: -h, --help show this help message and exit --file {bought,sold,inventory,all} Files to be resetted

Examples: python super.py reset --file inventory python super.py reset --file all