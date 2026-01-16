# class definition
class Song:
   def __init__(self,perfomer, title, album, year):
      self.perfomer = perfomer
      self.title = title
      self.album = album
      self.year = year
   def __str__(self):
      return f"Performer: {self.perfomer}\nTitle: {self.title}\nAlbum: {self.album}\nYear: {self.year}"
   

# object creation
song1 = Song('Ed Sheeran', "Hearts Don't Break Around Here", 'Divide', 2017)
song2 = Song('Queen', 'Bohemian Rhapsody', 'A Night at the Opera', 1975)

## object usage
print(song1)
print(song2)