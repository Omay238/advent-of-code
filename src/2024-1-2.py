vals1 = []
vals2 = []

for i in data.split("\n")[:-1]:
    vals1.append(int(i.split(" ")[0]))
    vals2.append(int(i.split(" ")[-1]))

vals1 = sorted(vals1)
vals2 = sorted(vals2)

out = 0

for i in vals1:
    out = out + i * vals2.count(i)

print(f"{year}-{day}-{part}: {out}")
