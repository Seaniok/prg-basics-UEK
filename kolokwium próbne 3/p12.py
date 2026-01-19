import re

def f(dates):
    # Dzielimy ciąg na pojedyncze daty używając przecinka
    date_list = dates.split(",")
    
    # Definiujemy wzorzec: 4 cyfry - 2 cyfry - 2 cyfry
    # ^ oznacza początek tekstu, $ oznacza koniec (żeby nie brać dat z dodatkowym tekstem)
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    
    # Tworzymy listę wynikową tylko z pasujących elementów
    result = [d for d in date_list if re.match(pattern, d)]
    
    return result

# Test
dates = "2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011"
print(f(dates)) 
# Wynik: ["1998-12-11", "2001-12-07"]