# Reverse Cipher program, modified. Based on:
# https://www.nostarch.com/crackingcodes (BSD Licensed)

print('Allow me to de/encipher your message, using the reverse cipher. \n What message do you have?')
message = input() # 'Three can keep a secret, if two of them are dead.'
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)