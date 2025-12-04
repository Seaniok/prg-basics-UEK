# total expenses for each category
# total expenses for each week
# total expenses for a month
# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food = 0
transport = 0
utilities = 0
total = 0

for row in monthly_expenses:
    food = food + row[0]
    transport = transport + row[1]
    utilities = utilities + row[2]
    total = total + sum(row)

week1 = sum(monthly_expenses[0])
week2 = sum(monthly_expenses[1])
week3 = sum(monthly_expenses[2])
week4 = sum(monthly_expenses[3])

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:', transport)
print('Utilities:', utilities)
print('Week 1:', week1)
print('Week 2:', week2)
print('Week 3:', week3)
print('Week 4:', week4)
print('---------------')
print('TOTAL:', total)