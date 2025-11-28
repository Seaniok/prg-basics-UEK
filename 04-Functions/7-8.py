# f(23) returns 6
# f(8) returns 3
# f(2) returns 1
# f(0) returns 0
def f(amount_to_pay):
    count = 0
    
    # 1. Handle the 5s
    # Use // for integer division (how many whole 5s fit?)
    count = count + amount_to_pay // 5 
    # Use % to find what is left over
    amount_to_pay = amount_to_pay % 5 
    
    # 2. Handle the 2s
    count = count + amount_to_pay // 2
    amount_to_pay = amount_to_pay % 2
    
    # 3. Handle the 1s (whatever is left)
    count = count + amount_to_pay 
    
    return count

print(f(8))

