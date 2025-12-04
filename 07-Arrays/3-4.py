# An array contains numbers: -15, 8, -31, 47, -2, 19. Create a program that finds and prints the maximum and minimum number. Do not use available functions.

array = [-15,8,-31,47,-2,19]

min_number = array[0]
max_number = array[0]

for x in array:
    if x < min_number:
        min_number = x
    if x > max_number:
        max_number = x

print('Min number:', min_number)
print('Max number:', max_number)