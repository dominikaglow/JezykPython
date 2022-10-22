seq1 = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
seq2 = [34, (2, 3, 1), [4, [33, 6, 75, (23, 48)]], [14, (5, 36, (45, 12))], 8, [9]]
res = []

def flatten(sequence):
    for elements in sequence:
        if isinstance(elements, (list, tuple)) == True:
            flatten(elements)
        else:
            res.append(elements)
    return res

print("Sekwencja 1: ", seq1)
print("Splaszczona lista wszystkich elementow sekwencji: ", flatten(seq1))

res.clear()
print("\n")

print("Sekwencja 2: ", seq2)
print("Splaszczona lista wszystkich elementow sekwencji: ", flatten(seq2))