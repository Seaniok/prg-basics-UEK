# f(1027) returns 0
# f(230335) returns 9
# f(513553007) returns 21

def f(number):
    wynik = 0
    number_s = str(number)
    for char in number_s:
        if number_s.count(char) > 1:
            char = int(char)
            wynik = wynik + char
    return wynik

print(f(230335))