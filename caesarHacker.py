# Caesar Cipher Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
message = 'f1IymwqI574qI6tm6I6tqIbqmo1owIfmux145\'Isq6m9m I64u2Is1q5I5uxw I5y116t,I6tq Im4qIx11wuzsI61In7 L'
message = 'mBBQIBhmRDhI!RDEBAh!PhEBh.O!TIBAh!ILKD,h"s!SBhVLRhBSBOhPBBKhPR.Eh!hTFIAh!KAh.LKCRPFKDhPMFABOhTB?j"hmBBQIBhE!Ah!IT!VPhQELRDEQhPMFABOPhTBOBhKB!Q,h.IB!K,h!KAhQFAVkhmRQhQE!QhJRPQhKLQh?BhQORB,h!QhIB!PQhKLQhFKhQEFPh.!PBkh'
message = 'qeFIP?eGSeECNNS,'                          # Ch06 Practice Question Line 1 = I love my kitty,
message = '5coOMXXcoPSZIWoQI,'                        # Ch06 Practice Question Line 2 = My kitty loves me,
message = 'avnl1olyD4l\'ylDohww6DhzDjhuDil,'          # Ch06 Practice Question Line 3 = Together we're happy as can be,

message = 'z.GM?.cEQc. 70c.7KcKMKHA9AGFK,'            # Ch06 Practice Question Line 4 = Though my head has suspicions,
message = '?MFYp2pPJJUpZSIJWpRdpMFY,'                 # Ch06 Practice Question Line 5 = That I keep under my hat,
message = 'ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K' # Ch06 Practice Question Line 6 = Of what if I shrank to the size of a rat.

message = 'Zfbi,!tif!xpvme!qspcbcmz!fbu!nfA'          # Ch06 Practice Question Line 7 = Yeah, she would probably eat me.


# Loop through every possible key:
for key in range(len(SYMBOLS)):
    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared:
    translated = ''

    # The rest of the program is almost the same as the Caesar program:
    # Loop through each symbol in message:
    for symbol in message:
        # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wraparound:
            if translatedIndex < 0:
                translatedIndex += len(SYMBOLS)

            # Append the decrypted symbol:
            translated += SYMBOLS[translatedIndex]

        else:
            # Append the symbol without encrypting/decrypting:
            translated += symbol

    # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))
