###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celcius = int(input('Enter the temperature in Celcius: '))
kelvin = celcius + 273.15  #Wzór na kelviny
fahrenheit = (celcius * 2) + 32  #Wzór na fahrenheit
print(f'The temperature in Kelvin is: {kelvin}')
print(f'The temperature in Fahrenheit is: {fahrenheit}')