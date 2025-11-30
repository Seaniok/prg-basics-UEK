# In a separate module, define a function that checks if the number is within the range <x, y>. The function returns a boolean value. Then, create a program and use the function you defined. Sample result:

# A number: 7
# Number 7 in the range <2,15>: yes

def f(x,y):
    for number in range(x,y+1):
        if number in range(x,y+1):
            return True
    return False

print(f(2,15))
range = input('Enter a range: ')
n = input('Enter a number: ')
print(f'Number {n} in the range {range}:', f(range))