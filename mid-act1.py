purchase_price = float(input("Enter the purchase price: "))
down_payment = 0.1 * purchase_price
balance = purchase_price - down_payment
rate = 0.12
monthly_payment = 0.05 * purchase_price

print("{:<15} {:<20} {:<15} {:<20} {:<15} {:<20}".format('Month', 'Total Balance', 'Interest', 'Principal', 'Payment', 'Balance Remaining'))

month = 1
while balance > 0:
    interest = balance * rate / 12
    principal = monthly_payment - interest

    if balance < monthly_payment:
        monthly_payment = balance + interest
        principal = balance

    print("{:<15} ${:<19.2f} ${:<14.2f} ${:<19.2f} ${:<14.2f} ${:<19.2f}".format(month, balance, interest, principal, monthly_payment, balance - principal))

    balance -= principal
    month += 1
