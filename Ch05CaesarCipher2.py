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

