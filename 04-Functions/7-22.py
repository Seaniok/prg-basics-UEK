# f("Internet of Things") returns "IoT"
# f("For Your Information") returns "FYI"
# f("Python) return "P"
def f(name):
    name = str(name)
    wynik = ""
    slowa = name.split()
    for char in slowa:
        wynik = wynik + slowa[0]
    return wynik
print(f("Internet of Things")) 
# Wynik: "IoT"