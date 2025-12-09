# 1. Define the initial array of zeros (as shown in the task)
array = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# 2. Use nested loops to modify the values
# We have 5 rows, so we loop from 0 to 4
for i in range(5):
    # We have 5 columns, so we loop from 0 to 4
    for j in range(5):
        # Calculate the multiplication value
        # We add 1 because indices start at 0 (so index 0 becomes multiplier 1)
        array[i][j] = (i + 1) * (j + 1)

# 3. Print the array nicely (to match the screenshot output)
for row in array:
    for number in row:
        # Print number with a bit of spacing (end=' ')
        # Use simple spacing or f-strings for alignment
        print(number, end=" ") 
    print() # Move to the next line after each row