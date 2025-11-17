###
# Program for testing built-in functions
#the largest number: 7,5,6,3,8,2
# the smallest number: 4,7,2,3,9,8
# length of the phrase: "computer science"
# letter read from the keyboard
# number representing the string "20303"
# binary string representing decimal number 304
# hexadecimal string representing decimal number 304
# integer representing the Unicode code of the € sign
# absolute value of -17
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

input_letter = input('Enter a letter: ')
print(input_letter)

chr_number = chr(20303)
print('Number representing the string is', chr_number)

bin_number = bin(304)
print('Binary number representing decimal 304 is', bin_number)

hex_number = hex(304)
print('Hexadecimal string representing decimal 304 is', hex_number)

repr_number = repr("\u20ac")
print('Int representing the Unicode code of the sign is', repr_number)

abs_number = abs(-17)
print('The absolute value of -17 is', abs_number)
