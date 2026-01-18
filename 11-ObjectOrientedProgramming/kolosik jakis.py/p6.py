def f(fnc,res):
    
    mean = filter(fnc,res)
    max_number = max(mean)
    mean = filter(fnc,res)
    min_number = min(mean)
    result = max_number - min_number
    return result

if __name__ == '__main__':
    print(f(lambda x: x>50, [95,90,20,50,70]))
    