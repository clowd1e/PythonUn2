import random
s = []
for i in range(10):
    s.append(random.randint(1, 100))

print(s)
def ParzystaLubNieParzysta(start, end):
    # if n % 2 == 0:
    #     print('Parzysta')
    # elif n % 2 != 0:
    #     print('Nie Parzysta')
    if start <= 0 or end > len(s):
        print('Błąd!')
    else:
        for i in s[start - 1:end]:
            if i % 2 == 0:
                print(i, 'Parzysta')
            elif i % 2 != 0:
                print(i, 'Nie Parzysta')

ParzystaLubNieParzysta(4, 7)