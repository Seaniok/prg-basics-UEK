# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN
# Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.

numbers_of_hours = int(input('Enter the number of hours of parking: '))
fee1 = 5
fee2 = 15
fee3 = 20

if numbers_of_hours >= 1 and numbers_of_hours <= 2:
    print(f'Your fee is {fee1}')
elif numbers_of_hours >= 3 and numbers_of_hours <= 6:
    print(f'Your fee is {fee2}')
elif numbers_of_hours > 6:
    print(f'Your fee is {fee3}')