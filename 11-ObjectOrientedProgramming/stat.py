from statki import Staty

def main():
    staty = Staty()
    
    staty.add(12,37,6,9,17)
    staty.display_number()
    staty.biggest()
    staty.smallest()
    staty.srednia()
    staty.display_info()
    
if __name__ == '__main__':
    main()