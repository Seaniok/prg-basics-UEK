# f(4) returns "*/*/*/*"
# f(1) returns "*"

def f(n):
    asterisks = '*' + (n-1) * '/*'
    return asterisks

print(f(4))