line = "Python wspiera różne paradygmaty programowania mianowicie obiektowy " \
       "imperatywny oraz w mniejszym stopniu funkcyjny"

listWords = line.split()
print(listWords)

maxLen = 0
maxWord = ""

for words in listWords:
    if(len(words) > maxLen):
        maxLen = len(words)
        maxWord = words

print("Najdluzszy wyraz: " + maxWord + ", jego dlugosc: ", maxLen)