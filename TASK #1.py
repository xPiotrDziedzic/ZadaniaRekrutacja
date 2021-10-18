def change(x):
    x = str(x)
    if int(x) < -2147483647 or int(x) > 2147483647: #sprawdzenie liczby 32bit
        return 0
    elif x[0] == "-": #liczby ujemne
        x2 = x[1:]
        x3 = "-" + x2[::-1]
        x4 = int(x3)
        print(x4)
        return x4
    else: #liczby dodatnie
        x5 = x[::-1]
        x6 = int(x5)
        print(x6)
        return x6


change(512)
change(-954)
