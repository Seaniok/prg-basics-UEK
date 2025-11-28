def sum_natural(n):
    count = 0
    n = int(n)
    for x in range(0,n+1):
        count = count + x
    return count
print(sum_natural(10))