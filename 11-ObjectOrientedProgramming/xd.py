import os

def wyswietl_menu():
    # --- TUTAJ MOŻESZ EDYTOWAĆ NAZWY SWOICH PUNKTÓW ---
    opcja1 = "Pocaluj mnie"
    opcja2 = "Planowa podroze"
    opcja3 = "Stranger Things"
    opcja4 = "Przytul mnie"
    opcja5 = "Wyjście z programu"
    # -------------------------------------------------

    while True:
        # Czyścimy konsolę (opcjonalne, dla estetyki)
        os.system('cls' if os.name == 'nt' else 'clear')

        print("==============================")
        print("          MENU OPCJI        ")
        print("==============================")
        print(f"1. {opcja1}")
        print(f"2. {opcja2}")
        print(f"3. {opcja3}")
        print(f"4. {opcja4}")
        print(f"5. {opcja5}")
        print("==============================")

        wybor = input("Wybierz punkt (1-5): ")

        if wybor == '1':
            print(f"Uruchomiono: {opcja1}")
            # Tu wpisz swój kod dla opcji 1
            print("\nPocałuj mnie natychmiast")
        elif wybor == '2':
            print(f"Uruchomiono: {opcja2}")
            # Tu wpisz swój kod dla opcji 2
            print("\nPlanowa podroze: \nMajorka, \nVietnam, \nIrlandia, \nWłochy")
        elif wybor == '3':
            print(f"Uruchomiono: {opcja3}")
            # Tu wpisz swój kod dla opcji 3
            print("\nNie wiem po co to, ale fuck BIlly")
        elif wybor == '4':
            print(f"Uruchomiono: {opcja4}")
            # Tu wpisz swój kod dla opcji 4
            print("\nPrzytul mnie natychmiast")
        elif wybor == '5':
            print("See you ")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
            import time
            time.sleep(5)

# Uruchomienie programu
if __name__ == "__main__":
    wyswietl_menu()