# In a separate module, define a function that checks if the number is within the range <x, y>. The function returns a boolean value. Then, create a program and use the function you defined. Sample result:

# A number: 7
# Number 7 in the range <2,15>: yes

def f(x,y):
    if x in range(x,y+1):
        return 'yes'
    return 'no'
print(f'Number 7 in the range <2,15>:', f(2,15))
