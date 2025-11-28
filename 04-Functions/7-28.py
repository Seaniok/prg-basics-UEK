# f("5233165554211") returns 5
# f("2133") returns 3

def f(dice):
    dice_s = str(dice)
    count = 0
    for char in dice_s:
        if dice_s.count(char)>1:
            return char
print(f('5233165554211'))