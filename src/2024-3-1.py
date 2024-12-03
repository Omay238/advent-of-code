import re

out = 0

for i in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data):
    out = out + int(i[0]) * int(i[1])

print(f"{year}-{day}-{part}: {out}")