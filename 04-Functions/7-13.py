# f(11) returns "1234567891011"
# f(4) returns "1234"

def f(n):
    wynik = ''
    for i in range(1, n+1):
        wynik = wynik + str(i)
    return wynik

print(f(4))