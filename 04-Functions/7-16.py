# f(5) returns 3
# f(9) returns 21

def f(n):
    # Krok 1: Przypadki bazowe (pierwsze dwie liczby są stałe)
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # Krok 2: Ustawienie początkowych wartości
    a = 0  # Pierwsza wartość
    b = 1  # Druga wartość
    
    # Krok 3: Pętla od 3. elementu do n-tego
    for i in range(3, n + 1):
        suma = a + b   # Obliczamy nową liczbę
        a = b          # Przesuwamy: 'a' przejmuje wartość 'b'
        b = suma       # 'b' przejmuje wartość nowej sumy
        
    # Krok 5: Zwrócenie wyniku
    return b

print(f(300))
        
        