arr = [
    [-38, 19], 
    [5,40],
    [-7,11],
    [29,16]
]
biggest = arr[0][0]
smallest = arr[0][0]
row_index_biggest = 0
column_index_biggest = 0
row_index_smallest = 0
column_index_smallest = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        current_number = arr[i][j]
        if current_number > biggest:
            biggest = current_number
            row_index_biggest = i
            column_index_biggest = j
        if current_number < smallest:
            smallest = current_number
            row_index_smallest = i
            column_index_smallest = j
print(biggest, row_index_biggest, column_index_biggest)
print(smallest, row_index_smallest, column_index_smallest)