price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
suma_przed = 0
print('Before discount:')
for key,value in price_list.items():
    print(key, '=', value)
    suma_przed = round(suma_przed + value,2)
print(f'Total value before discount: {suma_przed}')

suma_po = 0
print('After discount:')
for key,value in price_list.items():
    discount = round(value - value*0.10,2)
    suma_po = round(suma_po + (value-value*0.10),2)
    print(key, '=', discount)
print(f'Total value after discount: {suma_po}')