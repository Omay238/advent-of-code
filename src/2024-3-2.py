import re

out = 0

dos = list(re.finditer(r"do\(\)", data))
donts = list(re.finditer(r"don't\(\)", data))

for i in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", data):
    dos_index = len(data) + 1
    donts_index = 0
    for j in dos:
        if j.span()[0] < i.span()[0]:
            dos_index = j.span()[0]
    for j in donts:
        if j.span()[0] < i.span()[0]:
            donts_index = j.span()[0]
    if dos_index > donts_index:
        out = out + int(i.group(1)) * int(i.group(2))

print(f"{year}-{day}-{part}: {out}")