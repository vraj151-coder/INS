```python
import numpy as np


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


def generate_key(size=2):
    np.random.seed(40)
    key = np.random.randint(low=0, high=26, size=(size, size))
    while np.linalg.det(key) == 0:
        key = np.random.randint(low=0, high=26, size=(size, size))
    return key


key = generate_key()
cipher_text = encrypt("vraj", key)

print(f'The key is : \n\n {key}\n')
print(f'cipher text is : {cipher_text}')
```
