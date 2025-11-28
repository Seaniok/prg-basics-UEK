# f(1) returns 2
# f(5) returns 11

def f(n):
    licznik = 0
    for x in range(2,n):
        if n % x == 0:
            return False
        else:
            return n
print(f(1))