# f("integrated development environment") returns
# "integrateddevelopmentenvironment"
# f("A programming language is a system of notation for writing
# computer programs") returns
# "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"

def f(sentence):
    wynik = ""                 # 1. Pusty pojemnik na nowy tekst
    for char in sentence:      # 2. Pętla przez znaki
        if char != " ":        # 3. Jeśli to NIE jest spacja...
            wynik += char      # ...doklej znak do wyniku
    return wynik

print(f("integrated development environment"))
