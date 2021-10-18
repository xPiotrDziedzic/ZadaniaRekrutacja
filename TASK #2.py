tab = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"] #tablica liter



def phone(digits):
    digits1 = []

    for i in digits:
        digits1.append(int(i))
    n = len(digits1)

    result = []
    g = []
    for j in digits1:
        for h in tab[j]:
            h.strip()
            g.append(h)
    if n == 1: #jedna liczba
        print(g)
    elif n == 0: #brak liczb
        print(result)
    elif (digits1[0] == 7 or digits1[0] == 9) and (digits1[1] == 7 or digits1[1] == 9): #dwie liczby z 4 znakami
        a = range(0, 4)
        b = range(4, 8)
        for s in a:
            for o in b:
                d = g[s] + g[o]
                result.append(d)
        print(result)
    elif digits1[0] == 7 or digits1[0] == 9 and n > 1: #jedna liczba z 4 znakami na pierwszej pozycji
        a = range(0, 4)
        b = range(4, 7)
        for s in a:
            for o in b:
                d = g[s] + g[o]
                result.append(d)
        print(result)
    elif digits1[1] == 7 or digits1[1] == 9 and n > 1: #jedna liczba z 4 znakami na drugiej pozycji
        a = range(0, 3)
        b = range(3, 7)
        for s in a:
            for o in b:
                d = g[s] + g[o]
                result.append(d)
        print(result)
    else: #liczby z 3 znakami
        a = range(0, 3)
        b = range(3, 6)
        for s in a:
            for o in b:
                d = g[s] + g[o]
                result.append(d)
        print(result)


phone(digits='46')
phone(digits='')
phone(digits='2')
