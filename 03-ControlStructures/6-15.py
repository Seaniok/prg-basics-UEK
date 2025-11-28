# Enter EAN-13 article number: 5901230094938
# Article number is correct
# Article manufactured in Poland

def f(ean_number):
    ean_number = str(ean_number)
    if len(ean_number) != 13:
        print('Invalid number, try again')
    else:
        print('Article number in correct')
        if ean_number[:3] == '590':
            print('Article manufactured in Poland')
        else:
            print('Article not manufactured in Poland')
            
print(f('5901230094938'))