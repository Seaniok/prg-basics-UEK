# 7, 1 ,0 ,-1 , -4

# Number ... is positive
# Number ... is negative
# Number is 0

number = int( input('Enter a number: '))

if number < 0:
    print(f'Number {number} is negative ')
elif number == 0:
    print(f'Number is 0')
elif number > 0:
    print(f'Number {number} is positive')