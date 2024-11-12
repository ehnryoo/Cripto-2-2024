from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii

BLOCK_SIZE = 8

def adjust_key(key):
    key = key.encode('utf-8')
    print(f'    Llave ingresada (hex): {binascii.hexlify(key).decode('utf-8')}')
    if len(key) > 8:
        key = key[:8]
    elif len(key) < 8:
        key += get_random_bytes(8 - len(key))
    print(f'    Llave ajustada (hex): {binascii.hexlify(key).decode('utf-8')}')
    return key

def des3_encrypt(key, iv, plaintext):
    iv = iv.encode('utf-8')
    plaintext = plaintext.encode('utf-8')
    padded_text = pad(plaintext, BLOCK_SIZE)
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_text)
    return binascii.hexlify(ciphertext).decode('utf-8')

def des3_decrypt(key, iv, ciphertext):
    iv = iv.encode('utf-8')
    ciphertext = binascii.unhexlify(ciphertext)
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_padded_text, BLOCK_SIZE).decode('utf-8')
    return decrypted_text


print('Llaves (8 bytes)')
key1 = adjust_key(input("  Llave 1: "))
key2 = adjust_key(input("  Llave 2: "))
key3 = adjust_key(input("  Llave 3: "))

iv = input("IV (8 bytes para 3DES): ")
plaintext = input("Texto: ")

print("\n===========================\n")

key = key1 + key2 + key3

# Cifrar usando Triple DES
ciphertext = des3_encrypt(key, iv, plaintext)
print(f'Texto cifrado con 3DES (hex): {ciphertext}')
print('\n===========================\n')

# Descifrar usando Triple DES
decrypted_text = des3_decrypt(key, iv, ciphertext)
print(f'Texto descifrado con 3DES: {decrypted_text}\n')