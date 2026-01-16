def f(array):
    count = 0
    for username in array:
        if len(username) < 4 or len(username) > 12:
            continue
        is_valid = True
        for char in username:
            if not (char.isdigit() or char.islower() or char == '_'):
                is_valid = False
                break
            
        if is_valid:
            count += 1
    return count
            
    
print(f(['uek', 'water_7_x', 'anna.may', 'a_b_c_d_e_f']))