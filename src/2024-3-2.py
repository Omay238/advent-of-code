import re

out = 0

for i in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", data):
    if data[:i.span()[0]].rfind("do()") >= data[:i.span()[0]].rfind("don't()"):
        out = out + int(i.group(1)) * int(i.group(2))

print(f"{year}-{day}-{part}: {out}")