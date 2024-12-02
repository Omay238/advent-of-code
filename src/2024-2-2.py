out = 0

for i in data.split("\n")[:-1]:
    validS = False
    for k in range(0, len(i.split(" "))):
        pj = None
        dec = None
        valid = True
        l = i.split(" ")
        l.pop(k)
        for j in l:
            j = int(j)
            if pj is not None:
                if abs(j - pj) > 0 and abs(j - pj) < 4:
                    if j < pj:
                        if dec is None:
                            dec = True
                        elif dec == False:
                            valid = False
                    elif j > pj:
                        if dec is None:
                            dec = False
                        elif dec == True:
                            valid = False
                else:
                    valid = False
            pj = j
        if valid:
            validS = True
    if validS:
        out = out + 1

print(f"{year}-{day}-{part}: {out}")
