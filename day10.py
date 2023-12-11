f = open('input/day10.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

g = [[c for c in line] for line in lines]

dn = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(0, 1), (1, 0)],
    '.': [],
    'S': []
}

lb = 'LJ7F'

def n(coords):
    x, y = coords
    return set([(x + dx, y + dy) for dx, dy in dn[g[x][y]] if g[x + dx][y + dy] != '.'])

for x in range(len(g)):
    for y in range(len(g[x])):
        if g[x][y] == 'S':
            a = (x, y)
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == dy == 0: continue
                    if a in n((x + dx, y + dy)):
                        dn['S'] += [(dx, dy)]
            g[x][y] = [s for s, c in dn.items() if c == dn['S']][0]
            break
    else: continue
    break
      
l = {a: n(a)}
x, y = a
while True:
    for dxy in n((x, y)):
        dx, dy = dxy
        if (dx, dy) not in l.keys():
            l[(dx, dy)] = n((dx, dy))
            x, y = dx, dy
            break
    else: break
part1 = len(l) // 2

e = set()
for x in range(len(g)):
    i = 0
    b = False
    for y in range(len(g[x])):
        if (x, y) in l.keys():
            if g[x][y] in '|':
                i += 1
            if g[x][y] in lb:
                if b:
                    if g[x][y] == lb[lb.index(b) - 2]:
                        i += 1
                    b = False
                else:
                    b = g[x][y]
        elif i % 2:
            e.add((x, y))
part2 = len(e)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
