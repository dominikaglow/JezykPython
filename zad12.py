line = """Python to jezyk programowania wysokiego 
poziomu ogolnego przeznaczenia"""

finalword = ""

myList = line.split()

for words in myList:
    finalword = finalword + words[0]

print("Tekst: "+ line)

print("Slowo powstale z pierwszych liter tekstu: " + finalword)

finalwordrev = ""

myList = line.split()

for words in myList:
    finalwordrev = finalwordrev + words[-1]

print("Slowo powstale z ostatnich liter tekstu: " + finalwordrev)
