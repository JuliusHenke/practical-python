# report.py
#
# Exercise 2.4
import csv
import sys


def read_portfolio_file(filename):
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        next(rows)
        portfolio = []
        for row in rows:
            portfolio.append({
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2]),
            })
        return portfolio


def compute_portfolio_value(filename):
    total_portfolio_value = 0
    for holding in read_portfolio_file(filename):
        total_portfolio_value += holding['shares'] * holding['price']
    return total_portfolio_value


if len(sys.argv) == 2:
    filenameArgument = sys.argv[1]
else:
    filenameArgument = 'Data/portfolio.csv'

value = compute_portfolio_value(filenameArgument)
print('Total portfolio value:', value)
