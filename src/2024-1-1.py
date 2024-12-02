vals1 = []
vals2 = []

for i in data.split("\n")[:-1]:
    vals1.append(int(i.split(" ")[0]))
    vals2.append(int(i.split(" ")[-1]))

vals1 = sorted(vals1)
vals2 = sorted(vals2)

out = 0

for i, j in zip(vals1, vals2):
    out = out + abs(i - j)

print(f"{year}-{day}-{part}: {out}")
