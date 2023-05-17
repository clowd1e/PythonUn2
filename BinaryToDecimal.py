a = str(input('Type binary nimber: '))

def binaryToDecidimal():
    b = list(a)
    d = 0
    print(b)
    for i in range(1, len(b) + 1):
        d = d + (int(b[-i]) * 2**(i - 1))
    
    print(d)

binaryToDecidimal()