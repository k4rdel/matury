# zadanie 1
def plansza(n, m, A):

    P = [[False for _ in range(m + 1)] for _ in range(n + 1)]

    P[1][1] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i][j] == 0:
                P[i][j] = False
            else:
                if i == 1 and j != 1:
                    P[i][j] = P[i][j - 1]
                elif i != 1 and j == 1:
                    P[i][j] = P[i - 1][j]
                elif i != 1 and j != 1:
                    P[i][j] = P[i][j - 1] or P[i - 1][j]
    print(P[n][m])

# plansza(4, 4, [[None, None, None, None, None],
#         [None, 1, 1, 1, 1],
#         [None, 0, 0, 0, 1],
#         [None, 0, 0, 0, 1],
#         [None, 0, 0, 0, 1]])

# zadanie 2
def cyfry(n):
    i = 0
    b = 1
    c = 0
    while n > 0:
        a = int(n % 10)
        n = int(n / 10)
        if a % 2 == 0:
            c = int(c + b * (a / 2))
        else:
            c = c + b
            i += 1
        b = b * 10
    print(f"{c} ilosc wykonan {i}")

# cyfry(3131123)

# zadanie 3
#3.1
def nieparzysty(n):
    m = []
    for i in range(len(n)):
        if(int(n[i]) % 2 != 0):
            m.append(n[i])
    m = ''.join(m)
    print(m)

# nieparzysty("4312334")

#3.2
def skrot():
    count = 0
    nope = []
    lines = []
    with open("Dane-NF-2405/skrot.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    for x in lines:
        n = str(x)
        m = []
        for i in range(len(n)):
            if(int(n[i]) % 2 != 0):
                m.append(n[i])
        if m == []:
            count += 1
            nope.append(int(x))
        else:
            m = ''.join(m)

    print(f"{count}\n{max(nope)}")

# skrot()

#3.3
def skrot2():
    from math import gcd

    lines = []
    with open("Dane-NF-2405/skrot2.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    for x in lines:
        n = str(x)
        m = []
        for i in range(len(n)):
            if(int(n[i]) % 2 != 0):
                m.append(n[i])
        
        m = ''.join(m)

        if(gcd(int(n), int(m)) == 7):
            print(n)

# zadanie 4

#4.1
def liczby1():
    table = [[],[]]
    i = 0
    with open("Dane-NF-2405/liczby.txt", "r") as f:
        lines = f.readlines()
    
    firstline = lines[0].split()
    secondline = lines[1].split()
    
    for x in firstline:
        table[0].append(int(x))
    for x in secondline:
        table[1].append(int(x))

    for i in range(len(table[0])):
        for z in range(len(table[1])):
            if table[0][i] % table[1][z] == 0:
                i += 1
    print(i)

# liczby1()

#4.2
def liczby2():

    table1 = []
    with open("Dane-NF-2405/liczby.txt", "r") as f:
        lines = f.readlines()
    
    firstline = lines[0].split()
    
    for x in firstline:
        table1.append(int(x))
    
    table1 = sorted(table1, reverse=True)
    print(table1[100])

# liczby2()

#4.3


#4.4
