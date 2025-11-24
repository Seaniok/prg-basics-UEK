# the array
# number of elements
# first value
# second value
# last value
# last but one value (do not use negative index values)
# sum of the first and last value
# middle value
# all array values separated by a single space (use a loop statement)
###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]
sum = arr[0] + arr[-1]
print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
n = len(arr)
print('Last value', arr[n-1])
print('Last but one value', arr[n-2])
print('Sum of the first and last value', sum )
print('Middle value is', arr[len(arr) // 2])
element_space = ''
for element in arr:
    element = str(element)
    element_space = element_space + element + ' '
print(element_space)
   
