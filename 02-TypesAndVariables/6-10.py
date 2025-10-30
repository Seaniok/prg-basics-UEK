##
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(movie.upper())

# print title in small letters
print(movie.lower())

# print how many times the vowel "e" appears in the title
print('Vowel "e" appears:', movie.count('e'))

# print where in the text is the word "Lord"
print('Lord is at index:', movie.find('Lord'))

# print where in the text is the word "dragon"
print('dragon is at index:', movie.find('dragon'))