# 1. Twój słownik z regionami (przepisany ze zdjęcia)
regions = {
    'C': 'Kujawsko-pomorskie',
    'L': 'Lubelskie',
    'F': 'Lubuskie',
    'E': 'Łódzkie',
    'K': 'Małopolskie',
    'W': 'Mazowieckie',
    'O': 'Opolskie',
    'R': 'Podkarpackie',
    'B': 'Podlaskie',
    'G': 'Pomorskie',
    'S': 'Śląskie',
    'T': 'Świętokrzyskie',
    'N': 'Warmińsko-mazurskie',
    'P': 'Wielkopolskie',
    'Z': 'Zachodniopomorskie',
    'D': 'Dolnośląskie' 
}

# 2. Funkcja do wczytania pliku (lub stworzenia listy, jeśli pliku brak)

with open("vehicle.txt", "r") as file:
    vehicles = file.read()


# 3. Przygotowujemy licznik dla każdego województwa (na start same zera)
# Dzięki temu wypiszemy też te województwa, z których nie ma żadnego auta.
counts = {}
for province in regions.values():
    counts[province] = 0

# 4. Główna pętla zliczająca
for car in vehicles:
    if len(car) > 0:       # Zabezpieczenie przed pustymi liniami
        first_letter = car[0]  # Bierzemy pierwszą literę (np. 'W' z 'WA12345')
        
        # Sprawdzamy, czy ta litera jest w naszym słowniku
        if first_letter in regions:
            province_name = regions[first_letter] # Np. 'Mazowieckie'
            counts[province_name] += 1            # Zwiększamy licznik

# 5. Wypisujemy wynik
for province, count in counts.items():
    print(f"{province}: {count}")



            
        