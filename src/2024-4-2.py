sd = data.split()

out = 0

for i in range(len(sd)):
    for j in range(len(sd[i])):
        if sd[i][j] == "A":
            if 0 < i < len(sd) - 1 and 0 < j < len(sd[i]) - 1:
                if ((sd[i - 1][j - 1] == "M" and sd[i + 1][j + 1] == "S" or
                        sd[i - 1][j - 1] == "S" and sd[i + 1][j + 1] == "M") and
                        (sd[i - 1][j + 1] == "M" and sd[i + 1][j - 1] == "S" or
                        sd[i - 1][j + 1] == "S" and sd[i + 1][j - 1] == "M")):
                    out = out + 1

print(f"{year}-{day}-{part}: {out}")
