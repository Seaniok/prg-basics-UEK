# An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and prints the array and the arithmetic mean of array values. Use the “for” loop statement.

array = [15,8,31,47,2,19]

suma = sum(array)
count = 0
for x in array:
    count = count + 1
    srednia = suma / count
    
print(suma)
print(srednia)