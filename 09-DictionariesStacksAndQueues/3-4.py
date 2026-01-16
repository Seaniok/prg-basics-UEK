import queue

n = int(input('Enter a number: '))
reszta = 0
stack = queue.LifoQueue()
while n != 0:
    reszta = n % 2
    stack.put(reszta)
    n = n//2
        
while not stack.empty():
    binarka = stack.get()
    print(binarka, end = '')
    