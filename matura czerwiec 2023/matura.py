# zadanie 1
# 1
def iloczyn(x, y):
    if y == 1:
        print(x)
        return x
    else:
        k = int(y / 2)
        z = int(iloczyn(x, k))
        if y % 2 == 0:
            print(x, y, k, z, z + z)
            return z + z
        else:
            print(x, y, k, z, x + z + z)
            return x + z + z

# x, y = 112, 112
# iloczyn(x, y)

# 2.1

def stworzSufiksa(slowo):
    if(len(slowo) > 0):
        s = [' '] * (len(slowo) + 1)
    for x in range(len(slowo)):
        s[x + 1] = slowo[x:]
    s = sorted(s)
    return s

# slowo = 'xxxxxxxxxx'

# i = 0
# for x in stworzSufiksa(slowo):
#     print(i, x)
#     i += 1

def czyMniejszy(n, s, k1, k2):
    licznik = 0
    i = k1
    j = k2
    while i <= n and j <= n:
        licznik += 1
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return True, licznik
            else:
                return False, licznik
            
    if j <= n:
        return True, licznik
    else:
        return False, licznik

# x = [' ']

# print(czyMniejszy(len(slowo), (x + list(slowo)), 2, 5))

#2.2

def czyMniejszy2(n, s, k1, k2):
    i = k1
    j = k2
    while i <= n and j <= n:
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return True
            else:
                return False
    if j <= n:
        return True
    else:
        return False


def czyMniejszyZPliku(path):
    global table
    table = []
    with open(path, "r") as f:
        lines = f.readlines()
    
    for z in range(len(lines)):
        line = lines[z].split()
        for x in line:
            table.append(x)

    x = [' ']
    table[1] = x + list(table[1])

# czyMniejszyZPliku("matura czerwiec 2023\DANE\DANE_M\slowa3.txt")

# if czyMniejszy2(int(table[0]), table[1], int(table[2]), int(table[3])):
#     print("TAK")
# else:
#     print("NIE")

# 3.1
def anagram1(path):
    table = []
    with open(path, "r") as f:
        lines = f.readlines()
    
    for z in range(len(lines)):
        line = lines[z].split()
        for x in line:
            table.append(list(x))

    zrownowazone = 0
    prawiezrownowazone = 0
    for i in table:
        zera = 0
        jedynki = 0
        for l in range(len(i)):
            if i[l] == '0':
                zera += 1
            else:
                jedynki += 1
        if zera == jedynki:
            zrownowazone += 1
        elif jedynki - zera == 1:
            prawiezrownowazone += 1
        elif zera - jedynki == 1:
            prawiezrownowazone += 1
    
    print(zrownowazone, prawiezrownowazone)

# anagram = 'anagram'
# anagram1(f"matura czerwiec 2023\DANE\DANE_M\{anagram}.txt")

#3.2
def anagram2():
    from math import comb

    table = []
    anagram = 'anagram'
    with open(f"matura czerwiec 2023\DANE\DANE_M\{anagram}.txt", "r") as f:
        lines = f.readlines()
    
    for z in range(len(lines)):
        line = lines[z].split()
        for x in line:
            if len(x) == 8:
                table.append(list(x))
    
    table2 = [[0] * 2 for _ in range(len(table))]
    h = 0
    for i in table:
        zera = 0
        jedynki = 0
        for l in range(len(i)):
            if i[l] == '0':
                zera += 1
            else:
                jedynki += 1
        iloscSposobow = comb(7, zera)
        table2[h][0] = iloscSposobow
        table2[h][1] = ''.join(i)
        h += 1
    for i in range(len(table2)):
        if table2[i][0] == max(table2, key=lambda x: x[0])[0]:
            print(table2[i][1])
# anagram2()

#3.3
def anagram3():
    table = []
    table2 = []
    anagram = 'anagram'
    with open(f"matura czerwiec 2023\DANE\DANE_M\{anagram}.txt", "r") as f:
        lines = f.readlines()
    
    for z in range(len(lines)):
        line = lines[z].split()
        for x in line:
            table.append(int(x ,2))

    for z in range(len(table)):
        if z != len(table) - 1:
            table2.append(abs(table[z] - table[z+1]))
    print(bin(max(table2))[2:])

# anagram3()

# 3.4
def anagram4():
    table = []
    anagram = 'anagram'
    with open(f"matura czerwiec 2023\DANE\DANE_M\{anagram}.txt", "r") as f:
        lines = f.readlines()
    
    for z in range(len(lines)):
        line = lines[z].split()
        for x in line:
            table.append(str(int(x ,2)))
    
    bezZer = 0
    sumy = []
    for i in table:
        suma = 0
        cyfra = list(dict.fromkeys(i))
        if not '0' in cyfra:
            bezZer += 1
        for x in range(len(cyfra)):
            suma += int(cyfra[x])
        sumy.append([suma, i])
    print(f"{bezZer}\n{max(sumy)[1]}")
# anagram4()

print(int("E9967A", 16))