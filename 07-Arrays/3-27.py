# A two-dimensional array of size 2 by 4 contains integer numbers. Create a program that prints array values in rows and columns.

two_d = [
    [1,2,3,4],
    [2,6,7,8]
]

for row in two_d:
    for column in row:
        print(column, end = ' ')
    print()