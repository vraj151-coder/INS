import string


def encrypt(plain_text, k=3):
    plain_text = plain_text.lower()
    idx_to_letter = dict(list(enumerate(alphabets)))
    letter_to_idx = dict([(val, key) for (key, val) in idx_to_letter.items()])
    cipher_text = ""
    for letter in plain_text:
        idx_replace = (letter_to_idx[letter] + k) % 26
        char = idx_to_letter[idx_replace]
        cipher_text += char
    return cipher_text


def decrypt(cipher_text, k=3):
    cipher_text = cipher_text.lower()
    idx_to_letter = dict(list(enumerate(alphabets)))
    letter_to_idx = dict([(val, key) for (key, val) in idx_to_letter.items()])
    plain_text = ""
    for letter in cipher_text:
        idx_replace = (letter_to_idx[letter] - k) % 26
        char = idx_to_letter[idx_replace]
        plain_text += char
    return plain_text


alphabets = string.ascii_lowercase

res = encrypt("vraj")
print(res)

new_res = decrypt(res)
print(new_res)
