ciphertext = 'xubbemehbtcovhyudtxemqhuoek'

# for i in range(26):
#     M = ""
#     for char in ciphertext:
#         if ord(char)-i < 97:
#             M += chr((ord(char)-i)-97+122)
#         else: M += chr((ord(char)+i))
#     print(f"Shift {i}: {M}\n")

for char in ciphertext:
    if ord(char)-16 < 97:
        print(chr(123-97-(ord(char)-16)))
    else: print(chr(ord(char)-16))