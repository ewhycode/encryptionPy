import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#hide key               print("chars: chars")
#hide key from output   print(f"key: {key}")

#ENCRYPTION
plainText = input ("Enter a message to encrypt: ")
cipherText = ""

for letter in plainText:
    index = chars.index(letter)
    cipherText += key[index]

print(f"original message: {plainText}")
print(f"encrypted message: {cipherText}")

#DECRYPTION
cipherText = input ("Enter a message to encrypt: ")
plainText = ""

for letter in cipherText:
    index = chars.index(letter)
    plainText += chars[index]

print(f"encrypted message: {cipherText}")
print(f"original message: {plainText}")
 
 