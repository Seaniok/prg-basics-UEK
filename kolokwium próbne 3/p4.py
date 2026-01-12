def f(fnc,res):
    answers_correct = filter(fnc,res)
    lowest = min(answers_correct)
    answers_correct = filter(fnc,res)
    maxin = max(answers_correct)
    difference = maxin - lowest
    return difference


print(f(lambda x: x>30 and x<90,[95,90,20,50,70]))