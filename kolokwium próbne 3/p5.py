import re

def f(mnumbers):
    ok = '[+-]?[A-Da-d1-7]+'
    w = 0
    for numer in mnumbers:
        if re.fullmatch(ok,numer):
            w += 1
    return w


    