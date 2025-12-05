# An apple a day keeps the doctor away

# Create a module MyText, containing:

# A function that returns the number of words in the text
# A function that returns an ordered array of words, from longest to shortest
# A function that returns an alphabetically ordered array of words
# Then, write a program, call the functions and print results. Sample result:

# Text: An apple a day keeps the doctor away
# Number of words: 8
# Words from the longest: doctor,apple,…
# Words ordered alphabetically: a,An,apple,away,…

sentence = 'An apple a day keeps the doctor away'

def number(sentence):
    count = 0
    x = sentence.split()
    for char in x:
        count = count + 1
    return count

print(number('An apple a day keeps the doctor away'))

def ordered(sentence):
    splited_sentence = sentence.split()
    ordered_words = sorted(splited_sentence)
    return ordered_words

print(ordered('An apple a day keeps the doctor away'))

def longest_shortest(sentence):
    splited_sentence = sentence.split()
    n = len(splited_sentence)
    array = []
        
print(longest_shortest('An apple a day keeps the doctor away'))