def f(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token == '+':
            right = stack.pop()
            left = stack.pop()
            stack.append(left+right)
        elif token == '-':
            right = stack.pop()
            left = stack.pop()
            stack.append(left-right)
        else:
            stack.append(int(token))
            
    return stack[0]

if __name__ == "__main__":
    print(f("2 3 4 5 + - +"))       # Powinno zwrócić -4
    print(f("11 7 + 15 - 14 +"))    # Powinno zwrócić 17