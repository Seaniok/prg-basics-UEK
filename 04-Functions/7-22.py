# f("Internet of Things") returns "IoT"
# f("For Your Information") returns "FYI"
# f("Python) return "P"
def f(name):
    name = str(name)
    wynik = ""
    slowa = name.split()
    for slowo in slowa:
        wynik = wynik + slowo [0]
    return wynik
print(f("For Your Information")) 
# Wynik: "IoT"