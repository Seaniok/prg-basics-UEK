import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct


# Use a stack. Read the next characters of the expression. 
# Skip all but the brackets. If it is an opening bracket, put it on the stack. 
# If it is a closing bracket, get the item from the stack and compare whether it is a matching opening bracket.

def brackets_ok(expression):
   stack = queue.LifoQueue()
   for char in expression:
       if char == '(' or char == '[':
           stack.put(char)
       elif char == ')' or char == ']':
           if stack.empty():
               return False
           top = stack.get()
           
           if char == ')' and top != '(':
               return False
           if char == ']' and top != '[':
               return False
    
   return True #True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
   print('Brackets ok')
else:
   print('Brackets not okay')

if brackets_ok(expression2):
    print('Brackets ok')
else:
    print('Bracket not okay')