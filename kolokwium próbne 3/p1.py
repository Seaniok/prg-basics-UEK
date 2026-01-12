def f(word):
    word = str(word)
    wave_parts = []

    for x in range(len(word)):
        variant = word[:x].lower() + word[x].upper() + word[x + 1:].lower()
        wave_parts.append(variant)


    return '-'.join(wave_parts)

print(f('water'))
