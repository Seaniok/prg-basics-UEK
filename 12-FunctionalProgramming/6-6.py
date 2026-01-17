array = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

func = list(map(lambda x: f"{x[0].upper()}, {x[1]}", array))

print(*func, sep = '\n')