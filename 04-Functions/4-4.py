###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    x = abs(number)
    x_string = str(x)
    
    sum = 0
    for char in range(0,number + 1):
        digit = int(char)
        sum = sum + digit
    return sum
result = sum_digits(9)
print(f'The sum of the digits in the number {9} is', result)