import numpy as np


def encrypt(plain_text, key):
    n = len(key)
    key = np.array(key)
    plain_text = plain_text.upper()
    split_into_grp = [plain_text[i:i+n] for i in range(0, len(plain_text), n)]
    cipher_text = ""

    for val in split_into_grp:
        if len(val) != n:
            while len(val) != n:
                val += 'X'
        p = [ord(char) - ord('A') for char in val]
        p = np.array(p)
        prod = np.dot(key, p) % 26
        res = [chr(ord('A') + val) for val in prod]
        cipher_text += ''.join(res)

    return cipher_text


def mod_inverse(a, m):
    for i in range(26):
        if (a * i) % m == 1:
            return i
    return None


def decrypt(cipher_text, key):
    n = len(key)
    key = np.array(key)
    key_det = int(round(np.linalg.det(key))) % 26

    if key_det == 0 or mod_inverse(key_det, 26) is None:
        return "Key is not invertible."

    key_inv = np.round(np.linalg.inv(key) * key_det *
                       mod_inverse(key_det, 26)).astype(int) % 26

    cipher_text = cipher_text.upper()
    split_into_grp = [cipher_text[i:i+n]
                      for i in range(0, len(cipher_text), n)]
    plain_text = ""

    for val in split_into_grp:
        p = [ord(char) - ord('A') for char in val]
        p = np.array(p)
        prod = np.dot(key_inv, p) % 26
        res = [chr(ord('A') + val) for val in prod]
        plain_text += ''.join(res)

    return plain_text


def generate_key(size=2):
    while True:
        key = np.random.randint(26, size=(size, size))
        key_det = int(round(np.linalg.det(key))) % 26

        if key_det == 0 or mod_inverse(key_det, 26) is None:
            continue

        return key


key = generate_key()
plain_text = "vraj"
cipher_text = encrypt(plain_text, key)
decrypt_text = decrypt(cipher_text, key)

print(f'The key is:\n{key}')
print(f'cipher text is: {cipher_text}')
print(f'Decrypted text is: {decrypt_text}')
