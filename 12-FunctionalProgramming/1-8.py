initials = lambda name, surname: name[0] + surname[0]

imie = input('Enter your name: ')
nazwisko = input('Enter your surname: ')

checker = initials(imie, nazwisko)

print(checker)