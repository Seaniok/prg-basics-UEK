def avg_speed(distance, hours, minutes):
    total_hours = hours + (minutes / 60)
    return distance / total_hours

dist = int(input('Enter distance in km: '))
h = int(input('Enter numbers of travel hours: '))
m = int(input('Enter number of travel minutes: '))

speed = avg_speed(dist,h,m)
print(f'Average speed: {speed} km/h')