# f("+-+++-+---") returns True
# f("+-+-+-+-") returns False
# f("+-++-+--") returns False
# f("+-++-++-+---") returns True

def f(detector):
    count = 0
    detector = str(detector)
    for char in detector:
        if char == '+':
            count = count + 1
        if char == '-':
            count = count - 1
        if count == 3:
            return True
    return False
        
print(f('+-+-+-+-'))