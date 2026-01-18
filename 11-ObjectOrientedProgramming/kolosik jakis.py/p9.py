def f(car, order):
    if order == 1:
        # Sortowanie alfabetyczne według numeru rejestracyjnego (klucza słownika)
        return sorted(car, key=lambda x: list(x.keys())[0])
    elif order == 2:
        # Sortowanie według przejechanych kilometrów (wartości) - malejąco
        return sorted(car, key=lambda x: list(x.values())[0], reverse=True)

# Testowanie zgodnie z Twoimi zasadami (if __name__ == "__main__")
if __name__ == "__main__":
    cars = [{"KR333":138}, {"WL555":497}, {"DB444":341}, {"MC222":412}]
    
    print(f(cars, 1)) # Powinno zwrócić listę od DB444 do WL555
    print(f(cars, 2)) # Powinno zwrócić listę od 497 km do 138 km