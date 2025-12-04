# Define the function f(x,y), which returns the sum of numbers in the range <x,y> that are completely divisible by 2 and 3 and not divisible by 4. Sample result:

# f(1,20) returns 24
# f(10,30) returns 48

def f(x,y):
    wynik = 0
    for x in range(x,y+1):
        if x % 6 == 0 and x % 4 != 0:
            wynik = wynik + x
    return wynik

print(f(1,20))