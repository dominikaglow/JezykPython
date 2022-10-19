while(1):
    print("Podaj liczbe: ")
    x = input()
    if(x == "stop"):
        break
    else:
        xFl = float(x)
        print("Wprowadzona liczba x =", xFl)
        print("x^3 =", xFl**3, "\n")
