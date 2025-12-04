# f(23) returns 6
# f(8) returns 3
# f(2) returns 1
# f(0) returns 0
def f(amount_to_pay):
   count = 0
   
   count = amount_to_pay // 5
   amount_to_pay = amount_to_pay % 5
   
   count = count + amount_to_pay // 2
   amount_to_pay = amount_to_pay % 2
   
   count = count + amount_to_pay // 1
   amount_to_pay = amount_to_pay
   
   return count

print(f(8))
   
   
