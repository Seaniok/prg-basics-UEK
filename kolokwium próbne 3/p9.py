def f(uid):
    for username in uid:
        if uid.count(username) > 1:
            return False
    return True
print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"]))        