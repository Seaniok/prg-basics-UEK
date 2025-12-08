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
   telewizja.set_channel(5)
   telewizja.show_status()


if __name__ == "__main__":
   main() 