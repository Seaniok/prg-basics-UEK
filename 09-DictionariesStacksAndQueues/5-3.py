translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
user_input = input('Enter a word: ')

for key,value in translations.items():
    if user_input in key:
        print('Word in polish:', value)
if user_input not in key:
    print('Translation not possible')
    