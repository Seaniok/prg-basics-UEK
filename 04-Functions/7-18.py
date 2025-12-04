# f("integrated development environment") returns
# "integrateddevelopmentenvironment"
# f("A programming language is a system of notation for writing
# computer programs") returns
# "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"

def f(sentence):
    wynik = ''
    for char in sentence:
        if char != ' ':
            wynik = wynik + char
    return wynik

print(f('integrated development environment'))