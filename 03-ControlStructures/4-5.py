###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''
decrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    code=ord(char)
    # add one to the character's code
    code=code + 1
    # replace new character code with its
    # corresponding character (use chr())
    encrypted_text+=chr(code)
    # add encrypted character to encrypted text

for char in encrypted_text:
    code=ord(char)
    code=code - 1
    decrypted_text = decrypted_text + chr(code)
    

print(f'{plain_text}')
print(f'{encrypted_text}')
print(f'{decrypted_text}')