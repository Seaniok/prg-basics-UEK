from functools import reduce

numbers = [2,4,6,3,7,5]

func = list(filter(lambda x: x%2==0, numbers))
func_2 = lambda x,y: x+y

result = reduce(func_2, func)

print(result)