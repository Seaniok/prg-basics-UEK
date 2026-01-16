class Ebook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False
    
    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
    
    def change_page(self,pages):
        self.current_page = pages
    
    def display_status(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Page numbers: {self.pages}")
        if self.is_open:
            print(f"Current page: {self.current_page}")
        else:
            print(f"I'll read later")
    
    def read_pages(self, num):
        if self.is_open:
            self.current_page += num
        else:
            print("Error: You cannot read a closed book!")