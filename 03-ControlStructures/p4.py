def f(card_number):
    card_number = str(card_number)
    middle = '**********'
    card_number_fixed = card_number[0:2] + middle + card_number[12:16]
    return card_number_fixed

