#a = 3, b = 4, c = 5 --> volume = 94, surface area = 60
#a = 8, b = 1, c = 2 --> volume = 16, surface area = 52

###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a_string = input('a=')
b_string = input('b=')
c_string = input('c=')
a = int(a_string)
b = int(b_string)
c = int(c_string)
surface_volume = a*b*c
surface_area = 2*(a*b) + 2*(a*c) + 2*(b*c)
print(f'The volume of a cuboid with sides {a},{b},{c} is {surface_volume}.')
print(f'The area of a cuboid with sides {a},{b},{c} is {surface_area}.')