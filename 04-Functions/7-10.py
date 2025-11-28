# f(-7,8) returns 3
# f(-1,11) returns 0

def f(x,y):
    count = 0
    for x in range(x,y):
        if x == -8 or x == -6 or x == -4 or x == -2:
            count = count + 1
    return count

print(f(-7,8))
        