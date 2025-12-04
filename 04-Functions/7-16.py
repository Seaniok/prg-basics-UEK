# f(5) returns 3
# f(9) returns 21

def f(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    
    a = 0
    b = 1
    
    for x in range(3, n+1):
        suma = a + b
        a = b
        b = suma
    
    return b

print(f(9))
        
        