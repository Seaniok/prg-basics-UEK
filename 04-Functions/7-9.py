# f(3124,True) returns 6
# f(3124,False) returns 4
# f(20576,False) returns 12
# f(20576,True) returns 8
# f(13115,True) returns 0

def f(number, even):
    count = 0
    number = str(number)
    if even == True:
        for x in number:
            x = int(x)
            if x == 2 or x == 4 or x == 6 or x == 8:
                count = count + x
                
    if even == False:
        for x in number:
            x = int(x)
            if x == 1 or x == 3 or x == 5 or x == 7 or x == 9:
                count = count + x
    return count
                
    


print(f(3124,True))