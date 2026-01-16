from tv import TV

def main():
   # object creation
   telewizja = TV()


   # object usage
   telewizja.show_status()
   telewizja.turn_on()
   telewizja.show_status()
   telewizja.turn_off()
   telewizja.show_status()
   telewizja.show_status()
   lista = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
   telewizja.set_channels(5)
   telewizja.show_channels()


if __name__ == "__main__":
   main() 