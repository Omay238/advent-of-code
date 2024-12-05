sd = data.split()
#S  S  S
# A A A
#  MMM
#SAMXMAS
#  MMM
# A A A
#S  S  S

table = [
    [[1, 0], [2, 0], [3, 0]],
    [[0, 1], [0, 2], [0, 3]],
    [[1, 1], [2, 2], [3, 3]],
    [[-1, 0], [-2, 0], [-3, 0]],
    [[0, -1], [0, -2], [0, -3]],
    [[1, -1], [2, -2], [3, -3]],
    [[-1, 1], [-2, 2], [-3, 3]],
    [[-1, -1], [-2, -2], [-3, -3]],
]

out = 0

for i in range(len(sd)):
    for j in range(len(sd[i])):
        if sd[i][j] == "X":
            for k in table:
                if 0 <= i + k[2][0] < len(sd) and 0 <= j + k[2][1] < len(sd[i]):
                    if sd[i + k[0][0]][j + k[0][1]] == "M" and sd[i + k[1][0]][j + k[1][1]] == "A" and sd[i + k[2][0]][j + k[2][1]] == "S":
                        out = out + 1

print(f"{year}-{day}-{part}: {out}")
