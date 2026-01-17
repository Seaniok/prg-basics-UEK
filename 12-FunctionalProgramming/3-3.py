stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

result = list(map(lambda x: x[0]*x[1], stock))
result_v2 = sum(result)

print(f'Products in stock: {stock}')
print(f'Total value: {result_v2}')