def f(arr):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]
    
print(f([5,7,7,7,7,7,7,7]))