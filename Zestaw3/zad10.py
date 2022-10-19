dictNum = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def roman2int(num):
    result = 0
    i = 0
    while i < len(num):
        if i + 1 < len(num) and dictNum[num[i]] < dictNum[num[i+1]]:
            val = dictNum[num[i+1]] - dictNum[num[i]]
            result += val
            i += 2
        else:
            result += dictNum[num[i]]
            i += 1
    print(num + " -> ", result)

print("Podaj liczbe w systemie rzymskim: ")
num = input()
print("Wprowadzona liczba: " + num)

roman2int(num)
