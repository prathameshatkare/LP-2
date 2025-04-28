# write a java/c/c++/python program to implement DES algorithm

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
def des_encrypt(plain_text, key):
    key = key[:8].encode('utf-8')
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text
def des_decrypt(encrypted_text, key):
    key = key[:8].encode('utf-8')
    des = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = des.decrypt(encrypted_text)
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    return decrypted_text.decode('utf-8')
message = "TEJAS1608"
key = "mysecret"
print(f"Original Message: {message}")
encrypted = des_encrypt(message, key)
print(f"Encrypted (bytes): {encrypted}")
print(f"Encrypted (hex): {encrypted.hex()}")
decrypted = des_decrypt(encrypted, key)
print(f"Decrypted Message: {decrypted}")
