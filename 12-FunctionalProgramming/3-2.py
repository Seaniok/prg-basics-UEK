sentence = 'I completely agree with you'
splited_sentence = sentence.split()
result = list(map(lambda x: len(x), splited_sentence))
print(result)