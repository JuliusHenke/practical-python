# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
totalPaid = 0.0

first_month_of_year_six = 12 * 5 + 1
four_years_in_months = 4 * 12

extra_payment_start_month = first_month_of_year_six
extra_payment_end_month = first_month_of_year_six + four_years_in_months
extra_payment = 1000

currentMonth = 0
while principal > 0:
    currentMonth += 1
    monthsPaymentSum = 0
    if currentMonth in range(extra_payment_start_month, extra_payment_end_month):
        monthsPaymentSum += extra_payment
    monthsPaymentSum += payment
    principal = principal * (1 + rate / 12) - monthsPaymentSum

    if principal < 0:
        totalPaid += monthsPaymentSum + principal
        principal = 0
    else:
        totalPaid += monthsPaymentSum

    print(currentMonth, totalPaid, principal)

print('Total paid', totalPaid)
print('Total months', currentMonth)
