#r = 1 --> circumference = 6.28, area = 3.14
#r = 3 --> circumference = 18.84, area = 28.26

###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results
import math
pi = 3.14
r = int(input('Enter radius: '))
area = round(pi * r**2, 2)
circumference = round(2 * (pi * r), 2)
print(f'Circumference is: {circumference}')
print(f'Area is: {area}')
