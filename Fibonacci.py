# b = int(input('End of Fibonacci: '))

# def Fibonacci(end):
#     s = [0, 1]
#     if end == 0:
#         return [0]
#     else:
#         for i in range(1, end):
#             c = s[i] + s[i - 1]
#             s.append(c)
#     return s

# print(Fibonacci(b))

a = int(input('End of Fibonacci: '))

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(a))