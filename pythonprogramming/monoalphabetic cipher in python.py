def monoalpha(plaintext,key):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext=plaintext.upper()
    ciphertext=""
    for char in plaintext:
        if char in plaintext:
            index=alphabet.index(char)
            ciphertext+=key[index]
        else:
            ciphertext+=char
    return ciphertext

key = "QWERTYUIOPASDFGHJKLZXCVBNM"
plaintext = "HELLO WORLD."
ciphertext = monoalpha(plaintext, key)
print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)

            
