from math import floor

rule_text = data.split("\n\n")[0]
update_text = data.split("\n\n")[1]

rules = []

out = 0

for i in rule_text.split():
    rules.append((int(i.split("|")[0]), int((i.split("|")[1]))))

for i in update_text.split():
    update = list(map(int, i.split(",")))
    applicable_rules = []
    for j in range(len(rules)):
        if rules[j][0] in update and rules[j][1] in update:
            applicable_rules.append(rules[j])
    checked = []
    valid = True
    for j in update:
        for k in applicable_rules:
            if j == k[1] and k[0] not in checked:
                valid = False
        checked.append(j)
    if valid:
        out = out + update[floor(len(update)/2)]

print(f"{year}-{day}-{part}: {out}")
