# Transposition Cypher Encryption
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    # myMessage = 'Cenoonommstmme oo snnio. s s c  '
    myKey = 8
    # myKey = 4

    # myKey = 9
    # myMessage = "Underneath a huge oak tree there was of swine a huge company,"
    # myMessage = "That grunted as they crunched the mast: For that was ripe and fell full"
    # myMessage = "Then they trotted away for the wind grew high: One acorn they left, and no more might you spy."

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print(ciphertext + '|')

    # Copy the encrypted string in ciphertext to the clipboard:
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key

    # Loop through each column in ciphertext.
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length.
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list.
            ciphertext[column] += message[currentIndex]

            # Move the currentIndex over.
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)


# If Ch07TranspositionEncrypt.py is run (instead of imported as a module), call
# the main() function.
if __name__ == '__main__':
    main()
