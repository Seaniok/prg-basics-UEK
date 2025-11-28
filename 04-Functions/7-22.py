# f("Internet of Things") returns "IoT"
# f("For Your Information") returns "FYI"
# f("Python") returns "P"

def f(name):
    wynik = ""
    
    # 1. Rozbij zdanie na listę słów
    # "Internet of Things" zamieni się w -> ['Internet', 'of', 'Things']
    slowa = name.split()
    
    # 2. Przejdź przez każde słowo z osobna
    for slowo in slowa:
        # 3. Weź pierwszą literę tego słowa i dodaj do wyniku
        wynik = wynik + slowo[0]
        
    return wynik

print(f("Internet of Things")) 
# Wynik: "IoT"