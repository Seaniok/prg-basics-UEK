def f(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif char == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
    return stack[0]
            
if __name__ == "__main__":
    # Test cases from the exam PDF [cite: 49-51]
    print(f("23+"))           # Returns 5
    print(f("26+45-+"))       # Returns 7