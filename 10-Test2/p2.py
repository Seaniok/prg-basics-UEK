def f(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
        
if __name__ == "__main__":
    print(f([7, 7, 5, 7])) # Returns 5