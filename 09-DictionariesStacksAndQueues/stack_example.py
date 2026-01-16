import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
# cards.put('King of Hearts \u2665')    
# cards.put('Queen of Diamonds \u2666')  
# cards.put('Jack of Spades \u2660')
cards.put(2)
cards.put(3)
cards.put(7)
cards.put(4)
cards.put(1)
cards.put(9) #Przy dodawaniu zabiera dwie ostatnie liczby za pomoca funkcji .get() i printuje od 3 elementu od dołu
cards.put(8)     

num1 = cards.get()
num2 = cards.get()
suma = num1 + num2
print('Suma:', suma)

suma_reszty_liczb = 0

while not cards.empty():
    element = cards.get()
    suma_reszty_liczb = suma_reszty_liczb + element

print('Suma reszty liczb:', suma_reszty_liczb)

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# removes and prints elements from the top of the stack
while not cards.empty():
    card = cards.get()
    print(card)

"""
Note the order of the printed elements.
The last added element is printed first.
"""
