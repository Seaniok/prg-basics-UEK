# The credit card number consists of 16 digits. In a separate module, define a function hide(card_number) that masks the card number. The function returns a character string in which only the first two and the last four digits of the card number are visible. The remaining digits of the card number are replaced with an asterisk. Then, create a program that masks some credit card digits. Import the module with the created function. Finally, print the credit card number. Sample result:

# f("5290312400019022") returns "52**********9022"

def hide(card_number):
    card_number = str(card_number)
    card_number = card_number[0:2] + '**********' + card_number[12:17]
    return card_number
    
print(hide('5290312400019026'))