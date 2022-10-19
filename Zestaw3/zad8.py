inputStr1 = input("Wprowadz elementy pierwszej listy separujac je spacja: ")
listUser1 = inputStr1.split()
print("Wprowadzona lista: ", listUser1)

inputStr2 = input("Wprowadz elementy pierwszej listy separujac je spacja: ")
listUser2 = inputStr2.split()
print("Wprowadzona lista: ", listUser2)

listSame = []
for elem1 in listUser1:
    for elem2 in listUser2:
        if elem1 == elem2:
            if elem2 not in listSame:
