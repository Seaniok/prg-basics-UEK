final_grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

func = list(filter(lambda x: x>2, final_grades))

mean = sum((func) / len(func))

print('Arithmetic mean for grades <> 2.0 is', mean)