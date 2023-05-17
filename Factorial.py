def Silnia(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Silnia(n - 1) * n

print(Silnia(6))