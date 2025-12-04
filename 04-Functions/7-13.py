# f(11) returns "1234567891011"
# f(4) returns "1234"

def f(n):
    wynik = ''
    for char in range(1,n+1):
        char = str(char)
        wynik = wynik + char
    return wynik

print(f(11))   
    
    
        