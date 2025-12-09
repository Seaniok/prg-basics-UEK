def create_2d_arr(x, y):
    array = []
    # Loop 'x' times to create rows
    for i in range(x):
        # Create a single row with 'y' zeros
        row = [0] * y
        # Add the row to the main array
        array.append(row)
    return array

print(create_2d_arr(3,5))