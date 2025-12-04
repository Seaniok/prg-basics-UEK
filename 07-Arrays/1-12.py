categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_cost = max(expenses)

index = expenses.index(max_cost)

most_expensive_category = categories[index]

print('Most expensive category is:', most_expensive_category)