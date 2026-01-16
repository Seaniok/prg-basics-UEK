from thermometer import Thermometer

def main():
    thermometer = Thermometer()
    
    thermometer.open()
    thermometer.measure()
    thermometer.display_info()
    thermometer.close()
    
if __name__ == '__main__':
    main()