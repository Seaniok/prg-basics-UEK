# f(2,3, "+") returns 5
# f(2,3, "%") returns 2
# f(2,3, "**") returns 8
# f(2,3, "*") returns 6
# f(2,3, "-") returns -1

def f(number1, number2, operator):
    if operator == '+':
        wynikdodawania = number1 + number2
        return wynikdodawania
    if operator == '-':
        wynikodejmowania = number1 - number2
        return wynikodejmowania
    if operator == '%':
        wynikreszty = number1 % number2
        return wynikreszty
    if operator == '*':
        wynikmnozenia = number1 * number2
        return wynikmnozenia
    if operator == '**':
        wynikpotegowania = number1 ** number2
        return wynikpotegowania

print(f(2,3,'-'))
    