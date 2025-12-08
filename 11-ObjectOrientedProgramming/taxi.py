class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    
    def print_receipt(self):
       print(f"Distance is {self.distance}")
       print(f"Rate is {self.rate_per_km} ")
       print(f"Fare is {self.fare}")


def main():
    # your program
    ride_one = TaxiRide(2)
    ride_two = TaxiRide(5)

    print('Ride one receipt:')
    ride_one.calculate_fare(20)
    ride_one.print_receipt()
    
    print('Ride two receipt:')
    ride_two.calculate_fare(50)
    ride_two.print_receipt()


if __name__ == "__main__":
    main()
