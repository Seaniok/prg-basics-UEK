# Write a program that draws the function y = sin(x) for an angle value in the range 0-360 degrees.

import matplotlib.pyplot as plt
import math

x = []
y = []

for n in range(0, 361):
    x.append(n)
    radians = math.radians(n)
    y.append(math.sin(radians))
    
plt.plot(x,y)
plt.show()