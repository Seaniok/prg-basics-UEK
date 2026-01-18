def f(vname):
    
    if len(vname) < 1 or len(vname) > 5:
        return False
    
    if not (vname[0].isalpha() or vname[0] == '_'):
        return False
    for char in vname[1:]:
        if not (char.isalnum() or char == '_'):
            return False
        
    return True
    
if __name__ == '__main__':
    print(f('aBC'))