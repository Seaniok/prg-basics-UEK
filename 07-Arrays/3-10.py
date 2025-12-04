numbers1 = [4,36,12,28,9,44,5]
numbers2 = [5,1,36]

unique_numbers = []

for num in numbers1:
    if num not in numbers2:
        unique_numbers.append(num)
        
print('Only numbers in first array:', unique_numbers)