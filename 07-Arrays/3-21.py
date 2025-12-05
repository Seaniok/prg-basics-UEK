# whether all elements of the first array appear in the second array.
array_3 = []
def f(array1, array2):
    for x in array2:
        if array1 == array2:
            return True
    else:
        return False
    
print(f([2,3,4,5,6], [2,3,4,5,6,7,8]))