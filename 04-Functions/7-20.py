# f(1) returns 2
# f(5) returns 11

def f(n):
    count = 0
    num = 1
    
    while count < n:
        num = num + 1
        prime = True 
        
        
        for i in range(2,num):
            if num % i == 0:
                prime = False
                break
            
        if prime:
            count = count + 1
            
    return num

print(f(5))