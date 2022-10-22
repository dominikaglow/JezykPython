
def make_ruler(n):
    text = ""
    num = "0"
    res = ""
    param = 5 * int(n)

    for i in range(0, param + 1):
        if (i % 5) == 0:
            text += "|"
        else:
            text += "."
    res += text
    res += "\n"

    for j in range(1, (int(n) + 1)):
        num += str(j).rjust(5)
    res += num

    return res

def make_grid(rows, cols):
    text = ""

    for i in range(0, (2 * int(rows)) + 1):
        for j in range(0, (int(cols) * 4) + 1):
            if j % 4 == 0:
                if (i % 2) != 0:
                    text += "|"
                else:
                    text += "+"
                if j == int(cols) * 4:
                    text += "\n"
            else:
                if (i % 2) != 0:
                    text += " "
                else:
                    text += "-"
    return text


print("RULER")
print("Dlugosc 12:")
print(make_ruler(12))
print("Dlugosc 17:")
print(make_ruler(17))

print("\n")
print("GRID")
print("3 wiersze, 5 kolumn")
print(make_grid(3, 5))
print("8 wierszy, 4 kolumny")
print(make_grid(8, 4))