from ebook import Ebook

def main():
    ebook = Ebook("Road", "Cormac McCarthy", 265)
    
    
    ebook.display_status()
    ebook.read_pages(3)
    ebook.display_status()
    ebook.close()
if __name__ == '__main__':
    main()
    