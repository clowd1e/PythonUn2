def next():
    k = str(input('Chcesz skończyć? '))
    if k.lower().strip() == 'nie':
        Kalkulator()
    elif k.lower().strip() == 'tak':
        print('wyłączamy! Do zobaczenia UWU')
    else:
        print('Nie zrozumiałem 0_0')
        next()

def Kalkulator():
    fN = int(input('Podaj pierwszą liczbą: '))
    sN = int(input('Podaj drugą liczbą: '))
    znak = str(input('Wpisz znak: '))
    if znak.strip() == '+':
        print(fN + sN)
        next()
    elif znak.strip() == '-':
        print(fN - sN)
        next()
    elif znak.strip() == '*':
        print(fN * sN)
        next()
    elif znak.strip() == '/':
        print(float(fN / sN))
        next()
    else:
        print('Jeszcze nie mamy tego dzialania :( ')
        next()

Kalkulator()