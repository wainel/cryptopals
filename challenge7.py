import base64
from Crypto.Cipher import AES


my_file = open("7", "r")
ciphertext = base64.b64decode(my_file.read())
my_file.close()
key = b'YELLOW SUBMARINE'


def decrypt_ECB(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


plaintext = decrypt_ECB(ciphertext, key)
print(plaintext)