# Array: 2 3 2 5 8 1 9 8
# Unique elements: 3 5 1 9

array = [2,3,2,5,8,1,9,8]
unique_elements = [3,5,1,9]

wynik = []

for number in array:
    if number in unique_elements:
        wynik.append(number)
        
print(wynik)