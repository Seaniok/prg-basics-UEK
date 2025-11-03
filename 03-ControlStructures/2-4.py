###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 2 + 3
# 2 * 4
# 3 - 5
# 5 * 6
number1 = int( input('Enter number 1: '))
number2 = int( input('Enter number 2: '))
operator = input('Enter an operator: ')

if operator == '+' :
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2

# print result
print(f'{number1} {operator} {number2} = {result}')