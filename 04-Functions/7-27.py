# f("1082") returns True
# f("2035") returns True
# f("1114") returns False
# f("7071") returns False

def f(product_code):
    d1 = product_code[0]
    d2 = product_code[1]
    d3 = product_code[2]
    
    control_digit = product_code[3]
    
    suma = d1 + d2 + d3
    suma = int(suma)
    cotrol_digit = suma % 7 
    if control_digit == 0:
        return True
    
    return False

print(f('1082'))