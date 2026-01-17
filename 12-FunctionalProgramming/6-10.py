

import matplotlib.pyplot as plt

# 1. Dane wejściowe ze stacji pomiarowych
temp = {"Krakow":7, "Warszawa":-2, "Sopot":4, "Koszalin":-1, "Gdansk":5}

# 2. Użycie map() do stworzenia dwóch tablic danych (zgodnie ze wskazówką)
# Wyodrębniamy nazwy miast (oś X)
cities = list(map(lambda x: x, temp.keys()))
# Wyodrębniamy wartości temperatur (oś Y)
temperatures = list(map(lambda city: temp[city], cities))

# 3. Tworzenie wykresu słupkowego
plt.bar(cities, temperatures)

# 4. Dodawanie tytułu i opisów osi
plt.title("Temperatures recorded in cities")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")

# 5. Wyświetlenie wykresu
plt.show()