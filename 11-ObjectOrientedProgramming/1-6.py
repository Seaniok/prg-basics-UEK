class Smartphone:
    def __init__(self, model, producer, year, app):
        self.model = model
        self.producer = producer
        self.year = year
        self.app = app
    
    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_close = False
        
    def change(self,app):
        self.app_change = app
    
    def display_info(self):
        print(f"My phone is {self.model}")
        print(f"The producer of the phone is {self.producer}")
        print(f"The year it was produced is {self.year}")
        if self.is_open:
            print(f"Right now I'm using the {self.app_change} app")
        else:
            print(f"I'll use the phone later ")
    
def main():
    phone = Smartphone(
        "Iphone 11", "Apple", "2015", "Youtube"
    )
    
    phone.open()
    phone.change('Dualingo')
    phone.display_info()
    phone.close()
    
if __name__ == '__main__':
    main()