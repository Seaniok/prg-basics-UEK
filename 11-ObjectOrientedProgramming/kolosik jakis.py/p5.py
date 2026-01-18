class C:
    def __init__(self, sectors):
        self.sectors = sectors
        
    def m1(self, s, n):
        self.sectors[s] = n
        
    def m2(self, s):
        total = 0
        for char in s:
            if char in self.sectors:
                total += self.sectors[char]
        return total
    
if __name__ == "__main__":
    stadium = C({"A": 100, "B": 200, "C": 150})
    stadium.m1("A", 120)  # Zmiana fanów w A
    stadium.m1("D", 300)  # Dodanie sektora D
    print(stadium.m2("AD"))  # Powinno zwrócić 420 (120+300)
    print(stadium.m2("ABC")) # Powinno zwrócić 470 (120+200+150)