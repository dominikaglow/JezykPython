text = ""
num = "0"
print("Podaj dlugosc miarki:")
dl = input()
print("Wprowadzona dlugosc miarki:", dl)
param = 5 * int(dl)

for i in range(0, param + 1):
    if (i % 5) == 0:
        text += "|"
    else:
        text += "."

for j in range(1, (int(dl) + 1)):
    num += str(j).rjust(5)

print(text)
print(num)