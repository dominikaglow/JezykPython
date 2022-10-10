L = [4, 85, 3, 984, 1, 537, 75, 37, 2, 45, 74, 78, 96, 8]

text = ""

for elements in L:
    txtNum = str(elements)
    if(len(txtNum) < 3):
        txtNum = txtNum.zfill(3)
    text += txtNum

print("Lista L:", L)
print("Zbudowany napis: " + text)