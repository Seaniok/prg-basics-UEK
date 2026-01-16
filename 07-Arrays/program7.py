def f(array):
    count = 0
    for username in array:
        # 1. Sprawdź długość
        if len(username) < 4 or len(username) > 12:
            continue
        
        # 2. Załóż, że słowo jest poprawne
        is_valid = True
        
        # 3. Sprawdź każdy znak
        for char in username:
            # Prawidłowy warunek: islower() sprawdza, czy to mała litera
            if not (char.islower() or char.isdigit() or char == '_'):
                is_valid = False # Znaleziono błąd (np. kropkę)
                break            # Przerwij sprawdzanie tego słowa
        
        # 4. Jeśli flaga nadal jest True -> zalicz słowo (tylko raz!)
        if is_valid:
            count = count + 1
            
    return count

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
            
        