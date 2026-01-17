
avg_speed = lambda distance, hours, minutes: distance / (hours + (minutes / 60))


dist = int(input('Enter distance in km: '))
h = int(input('Enter number of travel hours: '))
m = int(input('Enter number of travel minutes: '))


result = avg_speed(dist, h, m)
print(f"Average speed: {result} km/h")