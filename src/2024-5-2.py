from math import floor

rule_text = data.split("\n\n")[0]
update_text = data.split("\n\n")[1]

rules = []

out = 0

for i in rule_text.split():
    rules.append((int(i.split("|")[0]), int((i.split("|")[1]))))

def fix(update, applicable_rules):
    checked = []
    valid = False
    really_valid = True
    for j in update:
        for k in applicable_rules:
            if j == k[1] and k[0] not in checked:
                valid = True
                really_valid = False
                update[update.index(k[0])] = k[1]
                update[update.index(k[1])] = k[0]
        checked.append(j)
    return [update, valid, really_valid]

for i in update_text.split():
    update = list(map(int, i.split(",")))
    applicable_rules = []
    for j in range(len(rules)):
        if rules[j][0] in update and rules[j][1] in update:
            applicable_rules.append(rules[j])
    valid = False
    fixed = fix(update, applicable_rules)
    valid = fixed[1]
    while not fixed[2]:
        fixed = fix(fixed[0], applicable_rules)
    if valid:
        out = out + fixed[0][floor(len(fixed[0])/2)]

print(f"{year}-{day}-{part}: {out}")
