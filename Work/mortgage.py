# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

first_month_of_year_six = 12 * 5 + 1
four_years_in_months = 4 * 12

extra_payment_start_month = first_month_of_year_six
extra_payment_end_month = first_month_of_year_six + four_years_in_months
extra_payment = 1000

current_month = 0
while principal > 0:
    current_month += 1
    months_payment_sum = 0
    if current_month in range(extra_payment_start_month, extra_payment_end_month):
        months_payment_sum += extra_payment
    months_payment_sum += payment
    principal = principal * (1 + rate / 12) - months_payment_sum

    if principal < 0:
        total_paid += months_payment_sum + principal
        principal = 0
    else:
        total_paid += months_payment_sum

    print(current_month, total_paid, principal)

print('Total paid', total_paid)
print('Total months', current_month)
