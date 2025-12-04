# A function that returns the second largest element in an array
# A function that returns the difference between the largest and smallest values in an array
# A function that returns the median of numbers in an array.
# Do not use built-in functions. The median is the middle value in the ordered sequence of numbers:

# A function that returns a two-element array containing the smallest and largest values in an array

# A function that returns array elements as a string, separated by the minus sign

# Then, write a program that for the sequence of numbers:

# 7,3,8,5,2
# calculates and prints results. Sample result:

# Numbers: 7,3,8,5,2
# Second largest number: 7 
# Median: 5
# Smallest and largest number: 2,8
# Numbers as a string: 7-3-8-5-2

def second_biggest(array):
    second_max_number = array[0]
    for x in array:
        if x > second_max_number:
            second_max_number = x - 1
    return second_max_number


def f(difference_array):
    max_number = difference_array[0]
    min_number = difference_array[1]
    wynik = 0
    for x in difference_array:
        if x < min_number:
            min_number = x
        if x > max_number:
            max_number = x
        wynik = max_number - min_number
    return wynik


def median(array):
    n = len(array)
    mediana = 0
    sorted_array = sorted(array)
    count = 0
    for x in sorted_array:
        count = count + 1
        if count % 3 == 0 or count % 5 == 0 or count % 7 == 0 or count % 9 == 0:
            mediana = sorted_array[n // 2]
        if count % 2 == 0:
            right_number = sorted_array[n // 2]
            left_number = sorted_array[n // 2 - 1]
            mediana = (right_number + left_number) / 2
    return mediana
        

def two_element(array):
    max_number = array[0]
    min_number = array[1]
    
    array_two = []
    
    for x in array:
        if x > max_number:
            max_number = x
        if x < min_number:
            min_number = x
    return [min_number, max_number]


def string(array):
    return "-".join(str(x) for x in array)

array = [7,3,8,5,2]

print(f'Numbers: {array}')
print(f'Second largest number: {second_biggest(array)}')
print(f'Median: {median(array)}')
print(f'Smallest and largest number: {two_element(array)}')
print(f'Numbers as a string: {string(array)}')