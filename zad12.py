line = "Python to jezyk programowania wysokiego" \
       " poziomu ogolnego przeznaczenia"
finalword = ""

myList = line.split()
print(myList)

for words in myList:
    print(words.split())
    finalword = finalword + words[0]

print("Slowo powstale z pierwszych liter tekstu: " + finalword)

finalwordrev = ""

myList = line.split()
print(myList)

for words in myList:
    print(words.split())
    finalwordrev = finalwordrev + words[-1]

print("Slowo powstale z ostatnich liter tekstu: " + finalwordrev)
