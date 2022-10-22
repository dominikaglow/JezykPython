
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        a = 0
        b = 1
        for i in range(0, n - 1):
            c = a + b
            a = b
            b = c
        return b

print("fibonacci(3) =", fibonacci(3))
print("fibonacci(5) =", fibonacci(5))
print("fibonacci(11) =", fibonacci(11))
print("fibonacci(16) =", fibonacci(16))
print("fibonacci(19) =", fibonacci(19))