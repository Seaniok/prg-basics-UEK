# Write a program that asks the user for their age and then checks which age group they belong to:

# Child: under 13
# Teen: 13 to 19
# Adult: 20 to 64
# Senior: 65 or older

ask = int(input('Enter your age: '))

if ask < 13:
    print('Child')
elif ask >= 13 and ask <= 19:
    print('Teen')
elif ask >= 20 and ask <= 64:
    print('Adult')
else:
    print('Senior')