text = ""

print("Podaj wysokosc prostokata(liczba kratek): ")
h = input()
print("Podaj szerokosc prostokata(liczba kratek): ")
w = input()

for i in range (0, (2 * int(h)) + 1):
    for j in range (0, (int(w) * 4) + 1):
        if j % 4 == 0:
            if(i % 2) != 0:
                text += "|"
            else:
                text += "+"
            if j == int(w) * 4:
                text += "\n"
        else:
            if (i % 2) != 0:
                text += " "
            else:
                text += "-"
print(text)
