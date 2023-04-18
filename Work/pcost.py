# pcost.py
#
# Exercise 1.27
import csv
import sys


def compute_portfolio_value(filename):
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        next(rows)
        total_portfolio_value = 0
        for row in rows:
            try:
                shares = int(row[1])
                share_price = float(row[2])
            except ValueError:
                print('WARN: Invalid number in following line:', row)
                continue
            total_portfolio_value += shares * share_price
        return total_portfolio_value


if len(sys.argv) == 2:
    filenameArgument = sys.argv[1]
else:
    filenameArgument = 'Data/portfolio.csv'

value = compute_portfolio_value(filenameArgument)
print('Total portfolio value:', value)
