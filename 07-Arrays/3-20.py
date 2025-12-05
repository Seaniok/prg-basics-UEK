arr = [7,9,2,4,5,6]
arr_even = []
arr_odd = []
for x in arr:
    if x % 2 == 0:
        arr_even.append(x)
    else:
        arr_odd.append(x)
        
print(arr_even + arr_odd)