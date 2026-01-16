class Staty:
    def __init__(self):
        self.array = []
        
    def add(self, *numbers):
        self.array.extend(numbers)
    
    def display_number(self):
        print("Numbers:", *self.array)
    
    def biggest(self):
        self.max_number = max(self.array)
    
    def smallest(self):
        self.min_number = min(self.array)
        
    def srednia(self):
        suma = 0
        for number in self.array:
            suma += number
        self.srednia_liczb = suma / len(self.array)
            
    def display_info(self):
        print(f'Biggest number: {self.max_number}')
        print(f'Smallest number: {self.min_number}')
        print(f'Arithmetic mean: {self.srednia_liczb}')
            
        
    