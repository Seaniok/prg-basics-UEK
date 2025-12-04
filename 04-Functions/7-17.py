# f("radar") returns True
# f("12-11-21") returns True
# f("book") returns False

def f(palindrome):
    palindrome = str(palindrome)
    for char in palindrome:
        if palindrome[::-1] == palindrome:
            return True
    return False

print(f('radar'))
    
