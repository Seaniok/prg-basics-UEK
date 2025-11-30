# f(-7,8) returns 3
# f(-1,11) returns 0

def f(x,y):
    count = 0
    for x in range(x,y):
        if x < 0 and x % 2 == 0:
            count = count + 1
    return count

print(f(-12,8))
        