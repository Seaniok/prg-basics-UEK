# f(1027) returns 0
# f(230335) returns 9
# f(513553007) returns 21

def f(number):
    number_s = str(number)  # Zamiana na tekst
    suma = 0
    
    # Pętla 1: Bierzemy każdą cyfrę po kolei
    for x in number_s:
        
        # --- RĘCZNE LICZENIE (zamiast .count()) ---
        licznik = 0
        for y in number_s:  # Pętla 2: Sprawdzamy całą liczbę od nowa
            if y == x:      # Jeśli trafimy na tę samą cyfrę...
                licznik += 1
        # ------------------------------------------

        # Jeśli naliczyliśmy więcej niż 1 wystąpienie, dodajemy do sumy
        if licznik > 1:
            suma += int(x)
            
    return suma

print(f(230335)) # Wynik: 9