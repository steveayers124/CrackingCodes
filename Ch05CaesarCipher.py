# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

# The string to be encrypted/decrypted:
message = 'This is my secret message.'
message = 'To make sure that the Peacock Tailors\' getaway trip goes silky smooth, they are looking to buy.'
message = 'Fly And Fall rose into the air, as unstoppable as a hurricane.'
message = 'Beetle Bug laughed as he crawled along, "Have you ever seen such a wild and confusing spider web?" Beetle had always thought spiders were neat, clean, and tidy. But that must not be true, at least not in this case.'

# The encryption/decryption key:
key = 13
key = 12
key = 37

# Whether the program encrypts or decrypts:
mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
        
        # Handle wraparound, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        
        translated += SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated += symbol

# Output the translated string:
print(translated)
pyperclip.copy(translated)
