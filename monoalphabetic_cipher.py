import string
import random


def encrypt(plain_text, k):
    cipher_text = ""
    for letter in plain_text:
        char = k[letter]
        cipher_text += char
    return cipher_text


def decrypt(cipher_text, k):
    k_reverse = dict([(val, key) for (key, val) in k.items()])
    plain_text = ""
    for letter in cipher_text:
        char = k_reverse[letter]
        plain_text += char
    return plain_text


alphabets = string.ascii_lowercase
alphabets_shuffle = [char for char in alphabets]
random.shuffle(alphabets_shuffle)
alphabets_shuffle = ''.join(alphabets_shuffle)

key = dict(list(zip(alphabets, alphabets_shuffle)))

res = encrypt("vraj", key)
print(res)

new_res = decrypt(res, key)
print(new_res)
