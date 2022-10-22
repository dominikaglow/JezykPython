
def odwracanieIter(L, left, right):
    if left < right:
        i = left
        j = right
        while i < j:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
            i  += 1
            j -= 1
        return L
    else:
        return []

def odwracanieRek(L, left, right):
    if left < right:
        l = L[left]
        r = L[right]
        L[left] = r
        L[right] = l
        del r, l
        left += 1
        right -= 1
        odwracanieRek(L, left, right)
        return L
    else:
        return []

L1 = [1, 2, 3, 4, 5]
print("Lista L1: ", L1)
print("odwracanieIter(L1, 0, 4): ", odwracanieIter(L1, 0, 4))
odwracanieIter(L1, 0, 4)
print("odwracanieRek(L1, 0, 4): ", odwracanieRek(L1, 0, 4))

print("\n")
L2 = [64, 759, 4, 28, 1, 95, 945, 73]
print("Lista L2: ", L2)
print("odwracanieIter(L2, 0, 5): ", odwracanieIter(L2, 0, 5))
odwracanieIter(L2, 0, 5)
print("odwracanieRek(L2, 0, 5): ", odwracanieRek(L2, 0, 5))

print("\n")
L3 = ["BMW", "Toyota", "Mercedes", "Lexus", "Audi", "Ford", "Volvo"]
print("Lista L3: ", L3)
print("odwracanieIter(L3, 0, 4): ", odwracanieIter(L3, 3, 6))
odwracanieIter(L3, 3, 6)
print("odwracanieRek(L3, 0, 4): ", odwracanieRek(L3, 3, 6))