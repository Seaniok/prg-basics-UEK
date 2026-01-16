def f(player1,player2):
    array = ['A', 'K', 'Q', 'J', 'T']

    sum1 = 0
    sum2 = 0

    for card in player1:
        if card in array:
            sum1 = sum1 + 10
        else:
            sum1 = sum1 + int(card)
    for card in player2:
        if card in array:
            sum2 = sum2 + 10
        else:
            sum2 = sum2 + int(card)
    return sum1 >= sum2

print(f("AJ972","AQT72"))
    