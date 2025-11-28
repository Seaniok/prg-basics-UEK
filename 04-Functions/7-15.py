# f("+-+++-+---") returns True
# f("+-+-+-+-") returns False
# f("+-++-+--") returns False
# f("+-++-++-+---") returns True

def f(detector):
    count = 0
    for x in detector:
        if x == '+':
            count = count + 1
        if x == '-':
            count = count - 1
        if count == 3:
            return True
        
    return False
        
print(f('+-++-++-+---'))