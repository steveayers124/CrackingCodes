# Caesar Cipher function
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

def caesarCipher(message, key, mode):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated += SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated += symbol

    return translated

message = 'This is my secret message.'
key = 13
mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.
translated = caesarCipher(message, key, mode)
print(translated)
pyperclip.copy(translated)
message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
translated = caesarCipher(message, 13, 'decrypt')
print(translated)
pyperclip.copy(translated)

message = '"You can show black is white by argument," said Filby, "but you will never convince me."'
translated = caesarCipher(message, 8, 'encrypt')
print(translated)
pyperclip.copy(translated)
message = '"gw3EkivE1pw5EjtiksEq1E5pq2mEj7Eizo3umv2,"E1iqlENqtj7,E"j32E7w3E5qttEvm4mzEkwv4qvkmEumH"'
translated = caesarCipher(message, 8, 'decrypt')
print(translated)
pyperclip.copy(translated)

message = '1234567890'
translated = caesarCipher(message, 21, 'encrypt')
print(translated)
pyperclip.copy(translated)
message = 'HIJKLMNOPQ'
translated = caesarCipher(message, 21, 'decrypt')
print(translated)
pyperclip.copy(translated)

message = 'Kv?uqwpfu?rncwukdng?gpqwijB'
translated = caesarCipher(message, 2, 'decrypt')
print(translated)
pyperclip.copy(translated)

message = 'XCBSw88S18A1S 2SB41SE .8zSEwAS50D5A5x81V'
translated = caesarCipher(message, 22, 'decrypt')
print(translated)
pyperclip.copy(translated)


