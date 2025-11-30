# f("ax15") returns False
# f("book123") returns False
# f("A2water3") returns True
# f("qwerty") returns True
# f("") returns False

def f(password):
    password = str(password)
    if len(password) < 6:
        return False
    
    for char in password:
        if password.count(char) > 1:
            return False
    return True 

print(f('""'))
        

