
seq1 = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
seq2 = [34, (2, 3, 1), [4, [3, 6, 75, (3, 4)]], [4, (5, 6, (4, 2))], 8, [9]]
def sum_seq(sequence):
    sum = 0
    for elements in sequence:
        if isinstance(elements, (list, tuple)) == True:
            sum += sum_seq(elements)
        else:
            sum += elements
    return sum


print("Sekwencja 1: ", seq1)
print("Suma elementow sekwencji: ", sum_seq(seq1))

print("\n")

print("Sekwencja 2: ", seq2)
print("Suma elementow sekwencji: ", sum_seq(seq2))