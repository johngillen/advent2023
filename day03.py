import re

f = open('input/day03.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 0
part2 = 0

lp, lc, lg = [], [], {}

for x, line in enumerate(lines):
    d = [int(n) for n in re.findall(r'\d+', line)]
    y = [m.start() for m in re.finditer(r'\d+', line)]
    for i, p in enumerate(d):
        lp += [p]
        lc += [(x, y[i])]

for n, p in enumerate(lp):
    x, y = lc[n]
    for dx in range(x - 1, x + 2):
        for dy in range(y - 1, y + len(str(p)) + 1):
            dx = min(dx, len(lines) - 1); dx = max(dx, 0)
            dy = min(dy, len(lines[0]) - 1); dy = max(dy, 0)

            if lines[dx][dy].isdigit(): continue

            if lines[dx][dy] == '*':
                if (dx, dy) not in lg:
                    lg[(dx, dy)] = []
                lg[(dx, dy)] += [p]

            if lines[dx][dy] != '.':
                part1 += p
                break
        else: continue
        break

for g in lg:
    if len(lg[g]) == 2:
        part2 += lg[g][0] * lg[g][1]

print(f'part 1: {part1}')
print(f'part 2: {part2}')
