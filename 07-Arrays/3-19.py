user_input = int(input('Enter a number: '))

def f(number, array):
    return [x for x in array if x > number]
print(f(user_input,[5,6,7,4,3,2,9,8,7,5]))