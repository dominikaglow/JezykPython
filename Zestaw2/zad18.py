num1 = 640900500020
num2 = -538083600260
strNum1 = str(num1)
strNum2 = str(num2)
count1 = 0
count2 = 0

for elements in strNum1:
    if(elements == "0"):
        count1 += 1

for elements in strNum2:
    if(elements == "0"):
        count2 += 1

print("Liczba cyfr zero w liczbie: ", num1, " wynosi: ", count1)
print("Liczba cyfr zero w liczbie: ", num2, " wynosi: ", count2)
