def f(player1, player2):
    sum1 = 0
    for card in player1:
        if card == 'A' or card == 'K' or card == 'J' or card == 'Q' or card == 'T':
            sum1 += 10
        else:
            sum1 += int(card)
    sum2 = 0
    for card in player2:
        if card == 'A' or card == 'K' or card == 'J' or card == 'Q' or card == 'T':
            sum2 += 10
        else:
            sum2 += int(card)
    return sum1 >= sum2

if __name__ == "__main__":
    # Test cases from the exam sheet
    print(f("AJ972", "AQT72")) # Should be False
    print(f("9532", "K8"))     # Should be True
            