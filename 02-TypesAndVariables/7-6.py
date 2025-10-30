#The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. Write a program that checks whether the vehicle speed entered from the keyboard is correct. Sample result:

#Enter vehicle speed: 158
#Speed is valid: False

vehicle_speed = input('Enter vehicle speed: ')
check_speed = int(vehicle_speed)
valid_speed = check_speed >= 40 and check_speed <= 140
print(f'Speed is valid: {valid_speed}')