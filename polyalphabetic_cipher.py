def encrypt(plain_text, key):
    cipher_text = ""
    for idx in range(len(plain_text)):
        char_val_1 = ord(plain_text[idx]) - ord('A')
        char_val_2 = ord(key[idx]) - ord('A')
        final_char_val = ord('A') + (char_val_1+char_val_2) % 26
        character = chr(final_char_val)
        cipher_text += character
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    for idx in range(len(cipher_text)):
        char_val = ord(key[idx]) - ord('A')
        if (ord(cipher_text[idx]) - ord('A')) < char_val:
            final_char_val = (ord(cipher_text[idx]) + 26) - char_val
        else:
            final_char_val = ord(cipher_text[idx]) - char_val
        character = chr(final_char_val)
        plain_text += character
    return plain_text


key = "VRAJ"
plain_text = "PARIKHDEMOTRYTEST"


def make_key(plain_text, key):
    idx = 0
    while len(key) < len(plain_text):
        idx = idx % len(key)
        key += key[idx]
        idx += 1
    return key


key = make_key(plain_text, key)
print(key)
res = encrypt(plain_text, key)
print(res)
print(decrypt(res, key))
