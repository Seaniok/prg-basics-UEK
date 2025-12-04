# An array contains integer numbers: 34,7,19,4,21,8. Create a program that calculates and prints the number of even values in the array. Use the ‘while’ loop statement.
arr = [34,7,19,4,21,8]
count = 0
for x in arr:
    if x % 2 == 0:
        count = count + 1
        print(x, end =', ')
        
print('Count is:', count)
    