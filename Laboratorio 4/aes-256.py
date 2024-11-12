from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

BLOCK_SIZE = 16

def adjust_key(key):
    key = key.encode('utf-8')
    print(f'  Llave ingresada (hex): {binascii.hexlify(key).decode('utf-8')}')
    if len(key) > 32:
        key = key[:32]
    elif len(key) < 32:
        key += get_random_bytes(32 - len(key))
    print(f'  Llave ajustada (hex): {binascii.hexlify(key).decode('utf-8')}')
    return key

def aes_encrypt(key, iv, plaintext):
    iv = iv.encode('utf-8')
    plaintext = plaintext.encode('utf-8')
    padded_text = pad(plaintext, BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_text)
    return binascii.hexlify(ciphertext).decode('utf-8')

def aes_decrypt(key, iv, ciphertext):
    iv = iv.encode('utf-8')
    ciphertext = binascii.unhexlify(ciphertext)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_padded_text, BLOCK_SIZE).decode('utf-8')
    return decrypted_text


key = adjust_key(input('Llave (32 bytes): '))
iv = input("IV (16 bytes): ")
plaintext = input("Texto: ")

print("\n===========================\n")

# Cifrar usando AES-256
ciphertext = aes_encrypt(key, iv, plaintext)
print(f'Texto cifrado con AES-256 (hex): {ciphertext}')
print('\n===========================\n')

# Descifrar usando AES-256
decrypted_text = aes_decrypt(key, iv, ciphertext)
print(f'Texto descifrado con AES-256: {decrypted_text}\n')

