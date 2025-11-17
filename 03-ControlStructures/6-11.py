product_price = 140
previous_price = 200
discount = ((previous_price - product_price)/previous_price)*100

print(f'Current product price: {product_price}')
print(f'Previous product price: {previous_price}')

if discount >= 10:
    print('Buy the product !!')
    print(f'Product price reduced by {discount}%')
else:
    print('No discounts !')

