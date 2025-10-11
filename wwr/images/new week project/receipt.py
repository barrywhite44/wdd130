# receipt.py
# Author: Christopher Barrywhite
# Date: October 2025
# 
# Enhancement: Added a “Return By” date 30 days in the future at 9:00 PM.

import csv
from datetime import datetime, timedelta

def main():
    try:
        # Read products.csv into a dictionary
        products_dict = read_dictionary("products.csv", 0)

        # Open request.csv and print receipt
        print("Inkom Emporium")

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip header row

            num_items = 0
            subtotal = 0

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                try:
                    product_info = products_dict[product_id]
                    product_name = product_info[1]
                    product_price = float(product_info[2])

                    line_total = product_price * quantity
                    num_items += quantity
                    subtotal += line_total

                    print(f"{product_name}: {quantity} @ {product_price:.2f}")

                except KeyError as e:
                    print("Error: unknown product ID in the request.csv file")
                    print(e)
                    return  # Stop further execution

        # Calculate totals
        sales_tax_rate = 0.06
        sales_tax = subtotal * sales_tax_rate
        total = subtotal + sales_tax

        # Print receipt summary
        print(f"Number of Items: {num_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print("Thank you for shopping at the Inkom Emporium.")

        # Print date and time
        current_date_and_time = datetime.now()
        print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))

        # Enhancement: Return-by date (30 days in the future, 9:00 PM)
        return_by = current_date_and_time + timedelta(days=30)
        return_by = return_by.replace(hour=21, minute=0, second=0)
        print(f"Return by: {return_by.strftime('%a %b %d %I:%M %p %Y')}")

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)

def read_dictionary(filename, key_column_index):
    """Read a CSV file into a dictionary using the specified key column index."""
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

if __name__ == "__main__":
    main()
