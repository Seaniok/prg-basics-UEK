#Amount  : 15.84
#VAT 23% :  3.64
import math
amount_string = input('Amount: ')
amount = float(amount_string)
vat = round(amount*0.23, 2 )
print(f'Amount: {amount}')
print(f'Vat 23%: {vat}')