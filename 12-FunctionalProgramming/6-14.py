bottles = [508,500,512,499,492,511,503,476,501,509]

mean = list(filter(lambda x: x < 500-10 or x > 500+10, bottles))
percentage = (len(mean) / len(bottles)) * 100
print('Bottle capacity: 500ml')
print('Filling tolerance: 2%')
print('Filled bottles:', *bottles)
print('Incorrectly filled:', percentage,'%')