def encrypt(plain_text, key=3):
    key = key % 26
    cipher_text = ""
    for char in plain_text:
        char_val = ord(char) + key
        if char.islower():
            if char_val > 122:
                char_val = ord('a') + (char_val-122)
            val = chr(char_val)
            cipher_text += val
        elif char.isupper():
            if char_val > 90:
                char_val = ord('A') + (char_val-90)
            val = chr(char_val)
            cipher_text += val
    return cipher_text


def decrypt(cipher_text, key=3):
    key = key % 26
    plain_text = ""
    for char in cipher_text:
        char_val = ord(char) - key
        if char.islower():
            if char_val < 97:
                char_val = ord('z') - (97 - char_val + 1)
            val = chr(char_val)
            plain_text += val
        elif char.isupper():
            if char_val < 65:
                char_val = ord('Z') + (65 - char_val + 1)
            val = chr(char_val)
            plain_text += val
    return plain_text


plain_text = "Vraj"

res = encrypt(plain_text)
print(res)

print(decrypt(res))
