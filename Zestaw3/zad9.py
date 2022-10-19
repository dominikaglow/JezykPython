L = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
resList = []

for elem1 in L:
    if len(elem1) == 0:
        resList.append(0)
    else:
        sumNum = 0
        for elem2 in elem1:
            sumNum += elem2
        resList.append(sumNum)

print(resList)
