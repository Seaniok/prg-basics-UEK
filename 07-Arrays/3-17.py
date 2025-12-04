my_Tuple = (50,20,40,50,30,50)
# Value: 50
# Number of occurrences: 3

count = 0

for x in my_Tuple:
    if my_Tuple.count(x) > 1:
        count = count + 1

print('Value: ', x)
print('Number of occurrences: ', count)
