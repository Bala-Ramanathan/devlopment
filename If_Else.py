Price = 1000000
is_good_credit = True

if is_good_credit:
    down_payment = 0.1 * Price
else:
    down_payment = 0.2 * Price

print(f"DownPayment = ${down_payment}")
