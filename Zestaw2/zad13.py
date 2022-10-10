line = "Python to jezyk programowania wysokiego" \
       " poziomu ogolnego przeznaczenia"
listLen = []
myList = line.split()

print("Tekst: " + line)

for words in myList:
    listLen.append(len(words))

print("Lista zawierajaca dlugosci poszczegolnych slow: ", listLen)

totalLen = sum(listLen)
print("Suma dlugosci wszystkich slow: ", totalLen)
