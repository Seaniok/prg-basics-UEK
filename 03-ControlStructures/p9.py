def f(sentence):
    samogłoski = 'a', 'e', 'i', 'o', 'u', 'y'
    count = 0
    for x in sentence:
        if x == 'a' or x=='e' or x == 'i' or x == 'o' or x == 'u' or x == 'y':
            count = count + 1
    return count

print(f('rabit'))