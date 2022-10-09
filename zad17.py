import numpy as np

line = "Python to jezyk programowania wysokiego" \
	       " poziomu ogolnego przeznaczenia"
listLen = []
dict = {}

lowLine = line.lower()
myList = lowLine.split()

print("Tekst: " + line + "\n")
print("Lista wyrazow do posortowania w kolejnosci alfabetycznej: ", myList)

sortedList = sorted(myList)
print("Lista wyrazow w kolejnosci alfabetycznej: ", sortedList, "\n")


for words in myList:
	wordLen = len(words)
	if words not in dict.keys():
		newElem = {words : wordLen}
		dict.update(newElem)

sortedVal = sorted(dict.values())

sortedArr = np.array(sortedVal)

sortedDict = {}

for i in sortedArr:
	for j in dict.keys():
		if(dict[j] == i):
			newElem = {j : dict[j]}
			sortedDict.update(newElem)

print("Wyrazy posortowane ze wzgledu na dlugosc: ")
print(sortedDict.keys())