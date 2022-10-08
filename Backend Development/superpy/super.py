import argparse
from handle_date import handle_date
from advance_time import advanceTime
from exportToCSV import export
from Buy import add_buy_to_inventory
from Sell import add_sell_to_inventory
from plot import plot_data
import calculateProfit
from reset_files import reset_files
import pandas as pd

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.


def handle_args(args):
    # for advancing the currint datetime:
    if args.command == "advancedTime":
        advanceTime(args.time)

    # Buy a product and create inventory:
    elif args.command == "buy":
        add_buy_to_inventory(
            id=id,
            product=args.product,
            quantity=args.quantity,
            price=args.price,
            buy_date=args.buy_date,
            exp_date=args.exp_date,
        )
    # Sell product and update inventory
    elif args.command == "sell":
        add_sell_to_inventory(
            product=args.product,
            price=args.price,
            quantity=args.quantity,
            sell_date=args.sell_date,
        )

    # Export data inventory to File:
    elif args.command == "export":
        export(selection=args.file, date=args.date)

    # Calculate profit:
    elif args.command == "profit":
        calculateProfit.calculate_profit(args.date)

    # Plot bar graph of the inventory:
    elif args.command == "plot":
        plot_data(args.file)

    # Reset selection of files:
    elif args.command == "reset":
        reset_files(args.file)


def main():
    
    # Creating program Superpy to keep track of Supermarket Inventory
    parser = argparse.ArgumentParser(
        prog="super.py", description="Keep track of supermarket inventory.")

    subparsers = parser.add_subparsers(help="type of action", dest="command")
    subparsers.required = True

    # Creating Parsers for argument -advanced time so you can advance the date with a given number (integer)
    advanceTime_parser = subparsers.add_parser(
        "advancedTime", help="Advanced the date of the program")
    advanceTime_parser.add_argument(
        "--add-time", type=int, dest="time", help="Advanced the date of the program")

    # Creating arguments for buying products. Required arguments are product, price, buy-date, expiration date.
    buy_parser = subparsers.add_parser("buy", help="Buy a product")
    buy_parser.add_argument("--product", type=str,
                            dest="product", help="product name", required=True)
    buy_parser.add_argument("--buy-price", type=float, dest="price",
                            help="buy price per product", required=True)
    buy_parser.add_argument(
        "--quantity", type=int, dest="quantity", help="quantity of product", default=1)
    buy_parser.add_argument("--buy-date", type=str, dest="buy_date",
                            help="product buy date (format YYYY-MM-DD)", required=True)
    buy_parser.add_argument("--exp-date", type=str, dest="exp_date",
                            help="product expiration date (format YYYY-MM-DD)", required=True)
    # Sell products. Required arguments are productname, price, sell-date.
    sell_parser = subparsers.add_parser("sell", help="Sell a product")
    sell_parser.add_argument(
        "--product", type=str, dest="product", help="product name", required=True)
    sell_parser.add_argument("--sell-price", type=float,
                             dest="price", help="sell price per product", required=True)
    sell_parser.add_argument(
        "--quantity", type=int, dest="quantity", help="quantity of product", default=1)
    sell_parser.add_argument("--sell-date", type=str, dest="sell_date",
                             help="product sell date (format YYYY-MM-DD)", required=True)

    # Export of inventory. Required filename and date you want the products in the inventory
    export_parser = subparsers.add_parser(
        "export", help="Export selection of data on a specific date")
    export_parser.add_argument("--file", type=str, dest="file", help="Data to be exported to .csv file",
                               choices=["expired", "bought", "sold"], required=True)
    export_parser.add_argument("--date", type=str, dest="date",
                               help="Choose date of interest(format YYYY-MM-DD)", required=True)
    # Profit calculations
    profit_parser = subparsers.add_parser(
        "profit", help="Calculate profit on a specific date")
    profit_parser.add_argument("--date", type=str, dest="date",
                               help="Choose date of interest(format YYYY-MM-DD)", required=True)

    # Plot bar graph of the inventory. It shows the amount of products in the inventory
    plot_parser = subparsers.add_parser(
        "plot", help="Plot bar graph of products in inventory, bought or sold list")
    plot_parser.add_argument("--file", type=str, dest="file", help="File to be plotted",
                             choices=["bought", "sold", "inventory"], required=True)

    # Reset selection of files.
    reset_parser = subparsers.add_parser(
        "reset", help="Reset selection of files or all files")
    reset_parser.add_argument("--file", type=str, dest="file", help="Files to be resetted",
                              choices=["bought", "sold", "inventory", "all"], default="all")

    # Linking the arguments to the linked functions. See handle_args
    args = parser.parse_args()
    return handle_args(args)


if __name__ == "__main__":
    main()
    
