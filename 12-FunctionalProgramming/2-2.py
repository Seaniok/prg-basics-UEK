sorting = lambda list: sorted(list, key = len)
names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']
print(*sorting(names), sep = '\n')