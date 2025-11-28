# f("ax15") returns False
# f("book123") returns False
# f("A2water3") returns True
# f("qwerty") returns True
# f("") returns False

def f(password):
    password_s = str(password)
    if len(password_s) < 6:
        return False
    for char in password_s:
        if password_s.count(char) > 1:
            return False
    return True

print(f('A2water3'))
        

