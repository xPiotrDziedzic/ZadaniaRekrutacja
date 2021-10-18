def justify(words, width):

    if not words: #pusta tablica wyrazy
        return [""]

    res = []
    cur = []
    num_letters = 0

    for w in words:
        if num_letters + len(w) + len(cur) > width:
            if len(cur) == 1:   #pierwszy wyraz w linii
                res.append(cur[0] + ' ' * (width - num_letters))
            else: #reszta wyrazów
                num_spaces = width - num_letters
                space_between, extra = divmod(num_spaces, len(cur) - 1)
                for i in range(extra):
                    cur[i] += ' '
                res.append((' '*space_between).join(cur))

            cur = []
            num_letters = 0

        cur.append(w)
        num_letters += len(w)
    res.append(' '.join(cur) + ' ' * (width - num_letters - len(cur) + 1))  #ostatnia linia
    return res


print(justify(words=['Hey', 'there', 'mate,', 'it`s', 'nice', 'to', 'finally', 'meet', 'you.'], width=16))
