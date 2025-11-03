###
# Credit card payment 
# 140, 499, 500, 501, 720 (for the last two amounts, there are no funds)
#
account_balance = 500
total_payment = int( input("Enter total payment: "))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')