import numpy as np
from math import ceil


def encrypt(plain_text, key):
    n = len(key)
    key = np.array(key)
    plain_text = plain_text.upper()
    spit_into_grp = [plain_text[i:i+n] for i in range(0, len(plain_text), n)]
    cipher_text = ""
    for val in spit_into_grp:
        if len(val) != n:
            while (len(val) != n):
                val += 'X'
        p = []
        for char in val:
            p.append(ord(char)-ord('A'))
        p = np.array(p)
        prod = np.dot(p, key) % 26
        res = [chr(ord('A') + val) for val in prod]
        cipher_text += ''.join(res)
    return cipher_text


def get_inverse(key):
    adjoint = np.matrix.getH(key) % 26
    det = ceil(np.linalg.det(key) % 26)
    print(adjoint)
    print(det)
    inv = 1
    while True:
        if (det*inv) % 26 == 1:
            break
        inv += 1
    print(inv)
    key_inv = adjoint * inv
    return key_inv


def decrypt(cipher_text, key):
    n = len(key)
    key = np.array(key)
    cipher_text = cipher_text.upper()
    spit_into_grp = [cipher_text[i:i+n] for i in range(0, len(cipher_text), n)]
    plain_text = ""
    key_inv = get_inverse(key)

    for val in spit_into_grp:
        p = []
        for char in val:
            p.append(ord(char)-ord('A'))
        p = np.array(p)
        prod = np.dot(p, key_inv) % 26
        res = [chr(ord('A') + val) for val in prod]
        plain_text += ''.join(res)
    return plain_text


def generate_key(size=2):
    np.random.seed(40)
    key = np.random.randint(low=0, high=26, size=(size, size))
    while np.linalg.det(key) == 0:
        key = np.random.randint(low=0, high=26, size=(size, size))
    return key


key = generate_key()
plain_text = "vraj"
cipher_text = encrypt(plain_text, key)
decrypt_text = decrypt(cipher_text, key)

print(f'The key is:\n{key}')
print(f'cipher text is: {cipher_text}')
print(f'Decrypted text is: {decrypt_text}')
