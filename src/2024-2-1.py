out = 0

for i in data.split("\n")[:-1]:
    pj = None
    dec = None
    valid = True
    for j in i.split(" "):
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
        out = out + 1

print(f"{year}-{day}-{part}: {out}")
