#Enter price: 24.72
#Enter discount %: 15
#Price with discount: 21.01
#Reduction: 3.71
import math
price_string = input('Enter price: ')
price = float(price_string)
discount_string = input('Enter discount: ')
discount = int(discount_string)
reduction = round(price * (discount/100), 2)
discount_price = round(price - reduction, 2)
print(f'The price before discount is {price}, the discount is {discount}%, the discount price is {discount_price} and the reduction is {reduction}.')