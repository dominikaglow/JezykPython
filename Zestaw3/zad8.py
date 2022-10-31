# inputStr1 = input("Wprowadz elementy pierwszej listy separujac je spacja: ")
# listUser1 = inputStr1.split()
# print("Wprowadzona lista: ", listUser1)
#
# inputStr2 = input("Wprowadz elementy pierwszej listy separujac je spacja: ")
# listUser2 = inputStr2.split()
# print("Wprowadzona lista: ", listUser2)
#

def findSame(list1, list2):
    listSame = []
    for elem1 in list1:
        for elem2 in list2:
            if elem1 == elem2:
                if elem2 not in listSame:
                    listSame.append(elem2)
                else:
                    continue
    return listSame

def findAll(list1, list2):
    listAll = []
    for elem1 in list1:
        listAll.append(elem1)
    for elem2 in list2:
        if elem2 not in listAll:
            listAll.append(elem2)
        else:
            continue
    return listAll

l1 = [4, 1, 2, 3, 4, 5, 6, 7]
l2 = [12, 5, 4, 1, 2, 6, 2, 4, 50, 6, 72]
print(findSame(l1, l2))
print(findAll(l1, l2))

l3 = ("Python", "język", "programowania", "wysokiego", "poziomu", "ogólnego", "przeznaczenia", "o", "rozbudowanym", "pakiecie", "bibliotek", "standardowych")
l4 = ("Python", "ogólnego", "o", "skladnia", "rozbudowanym", "wersja", "testowa", "standardowych")
print(findSame(l3, l4))
print(findAll(l3, l4))
