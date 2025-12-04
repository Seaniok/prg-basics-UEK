# f(1027) returns 0
# f(230335) returns 9
# f(513553007) returns 21

def f(number):
    wynik = 0
    number = str(number)
    for x in number:
        if number.count(x) > 1:
            x = int(x)
            wynik = wynik + x
    return wynik

print(f(230335))