###
# Sums numbers entered by user
#
total_sum = 0
counter = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    counter += 1
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    average = total_sum/counter

print(f"The total sum of the numbers is: {total_sum} and the average is {average}")