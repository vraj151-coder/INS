import string
import numpy as np


plain_text = "vraj"
alphabets = string.ascii_lowercase

diagram = [[0] * 5] * 5


def is_present(diagram, val):
    diagram_cpy = diagram.copy()
    diagram_cpy = np.array(diagram_cpy).flatten()
    # print(diagram_cpy)
    for i in diagram_cpy:
        if i == val:
            return True
    return False


for char in plain_text:
    for idx_i in range(5):
        for idx_j in range(5):
            if diagram[idx_i][idx_j] != 0:
                # print(diagram[idx_i][idx_j])
                continue
            present = is_present(diagram, char)
            if not present:
                diagram[idx_i][idx_j] = char

print(diagram)
