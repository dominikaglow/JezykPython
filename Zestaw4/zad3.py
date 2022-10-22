
def factorial(n):
    res = 1
    i = n
    while i > 0:
        res *= i
        i -= 1
    return res

print("factorial(5) =", factorial(5))
print("factorial(3) =", factorial(3))
print("factorial(17) =", factorial(17))
print("factorial(11) =", factorial(11))
