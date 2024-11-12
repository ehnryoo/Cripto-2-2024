from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

BLOCK_SIZE = 8

def adjust_key(key):
    key = key.encode('utf-8')
    print(f'  Llave ingresada (hex): {binascii.hexlify(key).decode('utf-8')}')
    if len(key) > 8:
        key = key[:8]
    elif len(key) < 8:
        key += get_random_bytes(8 - len(key))
    print(f'  Llave ajustada (hex): {binascii.hexlify(key).decode('utf-8')}')
    return key

def des_encrypt(key, iv, plaintext):
    iv = iv.encode('utf-8')
    plaintext = plaintext.encode('utf-8')
    if len(plaintext) % BLOCK_SIZE == 0:
        padded_text = plaintext
    else:
        padded_text = pad(plaintext, BLOCK_SIZE)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_text)
    return binascii.hexlify(ciphertext).decode('utf-8'), key, iv

def des_decrypt(key, iv, ciphertext):
    ciphertext = binascii.unhexlify(ciphertext)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    padding_length = decrypted_padded_text[-1]
    decrypted_text = unpad(decrypted_padded_text, BLOCK_SIZE)
    return decrypted_text.decode('utf-8')

key = adjust_key(input('Llave (8 bytes): '))
iv = input('IV (8 bytes): ')
plaintext = input('Texto: ')

print('\n===========================\n')

ciphertext, adjusted_key, iv = des_encrypt(key, iv, plaintext)
print(f'Texto cifrado (hex): {ciphertext}')
print('\n===========================\n')

decrypted_text = des_decrypt(adjusted_key, iv, ciphertext)
if decrypted_text is not None:
    print(f'Texto descifrado: {decrypted_text}\n')