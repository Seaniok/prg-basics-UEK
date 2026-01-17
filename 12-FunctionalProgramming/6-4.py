array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

func = list(map(lambda x: pow(x,3), array))

print(*func)