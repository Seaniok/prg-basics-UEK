###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    x = abs(number)
    x_string = str(x)
    
    sum = 0
    for char in x_string:
        digit = int(char)
        sum = sum + digit
    return sum
any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is', result)