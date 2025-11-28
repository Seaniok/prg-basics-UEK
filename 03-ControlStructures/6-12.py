# In one of the online stores, a 25% discount is charged for each product purchased over two. Write a program that calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard. Sample result:

# Number of products purchased: 5
# Product price: 40
# Amount to pay: 170.00

number_of_products = int(input('How many products would you like to buy: '))
product_price = int(input('What is the price of the products: '))
discount = product_price - (product_price*0.25)
if number_of_products > 2:
    amount = (product_price*2) + ((number_of_products-2)*discount)
else:
    amount = number_of_products * 40 

print(f'Number of products purchased: {number_of_products}')
print(f'Product price: {product_price}')
print(f'Amount to pay: {amount}')