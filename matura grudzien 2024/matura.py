#zadanie 1
def J(n):
    binary = str(bin(n)[2:])
    print(binary)
    table = []

    for x in range(len(binary)):
        if binary[len(binary) - x - 1] == '1':
            table.append(x + 1)

    print(table)
# J(19)

#zadanie2
def F(x, p):
    if x == 0:
        return 0 
    else:
        c = x % p
        if c % 2 == 1:
            return F(x // p, p) + c
        else:
            return F(x // p, p) - c
# print(F(97, 4))

#zadanie 3
def liczbyCzterocyfrowe():
    from math import sqrt

    lines = []
    with open('matura grudzien 2024\Dane-2412\liczby.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())
    squares = []
    for x in lines:
        if sqrt(int(x)) % 1 == 0:
            squares.append(x)

    print(squares[0], len(squares))
# liczbyCzterocyfrowe()

def dzielniki():
    lines = []
    with open('matura grudzien 2024\Dane-2412\liczby.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    dzielnikitabela = []
    for z in lines:
        liczba = int(z)
        dzielnikiLiczby = []
        for x in range(liczba - 1):
            if liczba % (x + 1) == 0:
                dzielnikiLiczby.append(int(x + 1))
        dupa = []
        for u in dzielnikiLiczby:
            ilePierwszych = 0
            for i in range(u):
                if u % (i + 1) == 0:
                    ilePierwszych += 1
            if ilePierwszych == 2:
                dupa.append(u)
        if len(dupa) >= 5:
            dzielnikitabela.append(liczba)
    print(dzielnikitabela)
# dzielniki()

#3.3
def zadanie33():
    lines = []
    with open('matura grudzien 2024\Dane-2412\liczby.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    mniejsza = 0
    wieksza = 0
    rowna = 0

    for line in lines:
        line = list(str(line))
        najwieksza = int(''.join((sorted(line))))
        najmniejsza = int(''.join(sorted(line, reverse=True)))
        roznica = abs(najwieksza - najmniejsza)
        if roznica > int(''.join((line))):
            wieksza += 1
        elif roznica < int(''.join((line))):
            mniejsza += 1
        else:
            rowna += 1
    print(mniejsza, wieksza, rowna)
zadanie33()

#4.1
def prostokaty():
    lines = []
    pola = []
    with open('matura grudzien 2024\Dane-2412\prostokaty_przyklad.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())
prostokaty()