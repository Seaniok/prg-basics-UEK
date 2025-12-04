# f("101101") returns True
# f("1311a10100") returns False

def f(binary_number):
    binary_number = str(binary_number)
    for char in binary_number:
        if char != '1' and char != '0':
            return False
    return True

print(f('1311a10100'))