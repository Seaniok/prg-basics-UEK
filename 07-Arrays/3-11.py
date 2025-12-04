# Create a program that sorts elements of an array containing integer numbers. Apply the Bubble Sort sorting algorithm. Define a function bubblesort(array) that returns the sorted array. Try to sort and print any three arrays.
def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubblesort([2,3,4,5,75,745,522,9,8,5]))
print(bubblesort([2,3,4,6,1,9,0,65,89,21,56]))