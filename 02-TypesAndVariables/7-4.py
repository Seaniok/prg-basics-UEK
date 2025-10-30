#Enter tree circumference in cm: 120 
#Tree can be cut down: False
#Then, check if the program works correctly. There are several trees in the garden with the given circumferences in cm. Which trees can be cut down?
#
#Tree 1: 160 Tree 2: 90 Tree 3: 230 Tree 4: 120
import math
tree_circumference = input('Enter tree circumference: ')
tree_circumference_int = int(tree_circumference)
tree_diameter = tree_circumference_int/math.pi >= 50
print(f'Tree can be cut down: {tree_diameter}')