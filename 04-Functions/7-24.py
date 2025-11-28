# f("2+3") returns 5
# f("3+8+1") returns 12
# f("2+3-4+5-0") returns 6

def f(expression):
    return eval(expression)

print(f("2+3-4+5-0")) # Wynik: 6