a = int(input('Type start: '))
b = int(input('Type end: '))

def findPrimeNumbers(start, end):
    for i in range(start, end + 1):
        if i == 2:
            print(2)
        elif i == 1:
            pass
        elif i % 1 == 0 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 or i == 3 or i == 5 or i == 7:
            print(i)

findPrimeNumbers(a, b)