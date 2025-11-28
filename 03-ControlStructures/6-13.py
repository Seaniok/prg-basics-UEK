# Enter car speed: 38
# Warning: invalid car speed!!

# Use the following variables in your program:

# car_speed
# speed_limit_min
# speed_limit_max


car_speed = int(input('Enter your car speed: '))

speed_limit_min = car_speed < 40
speed_limit_max = car_speed > 140

if speed_limit_min:
    print('Warning: invalid speed')
elif speed_limit_max:
    print('Warning: invalid speed')
else:
    print('Good boy')