def f(fnc, prod):
    mean = list(map(fnc, prod))
    return mean

print(f(lambda x: "id:"+x[:2],["water","cheese","tomato"]))