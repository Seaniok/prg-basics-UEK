# Number: 23
# Array: 15 38 7 23 14
# Result: number 23 appears in the array

def occurs(number, array):
    wynik = 0
    if number in array:
        return True
    else:
        return False
    
number = int(input('Number: '))

my_array = [15,38,7,23,14]

print(my_array)

if occurs(number,my_array):
    print(f'Result: number {number} appears in the array.')
else:
    print(f"Result: number {number} doesn't appear in the array.")







