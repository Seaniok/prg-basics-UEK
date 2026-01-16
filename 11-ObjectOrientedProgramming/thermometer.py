import random
class Thermometer:
    def __init__(self):
        self.is_open = False
        self.temperature = 0
    
    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
        
    def measure(self):
        self.temperature = random.randint(34,42)
    
    def display_info(self):
        if self.temperature >= 37 and self.temperature < 41:
            print(f'Temperaure: {self.temperature} (fever)')
        if self.temperature >= 41:
            print(f"Temperature: {self.temperature} CRITICAL TEMPERATURE !!")
        if self.temperature < 37:
            print(f'Temperature: {self.temperature}')