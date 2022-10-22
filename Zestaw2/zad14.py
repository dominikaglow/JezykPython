line = "Python to jezyk programowania \nwysokiego poziomu     ogolnego \nprzeznaczenia"

listWords = line.split()
print("Tekst: " + line + "\n ")

maxLen = 0
maxWord = ""

for words in listWords:
    if(len(words) > maxLen):
        maxLen = len(words)
        maxWord = words

print("Najdluzszy wyraz: " + maxWord + ", jego dlugosc: ", maxLen)
