f = open('input/day11.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 0
part2 = 0

grid = [[c for c in line] for line in lines]

rr = [i for i, row in enumerate(grid) if not any(c != '.' for c in row)]
rc = [i for i, column in enumerate(zip(*grid)) if not any(c != '.' for c in column)]

while rr:
    grid.insert(rr.pop(), ['X'] * len(grid[0]))

while rc:
    c = rc.pop()
    for r in range(len(grid)):
        grid[r].insert(c, 'X')

lg = set([(x, y) for x, row in enumerate(grid) for y, char in enumerate(row) if char == '#'])

dg1, dg2 = {}, {}
for g in lg:
    dg1[g] = {}
    dg2[g] = {}
    for gg in lg:
        if g == gg: continue
        if gg in dg1 and g in dg1[gg]: continue

        dg1[g][gg] = abs(g[0] - gg[0]) + abs(g[1] - gg[1])
        dg2[g][gg] = abs(g[0] - gg[0]) + abs(g[1] - gg[1])

        for i in range(min(g[0], gg[0]), max(g[0], gg[0])):
            if grid[i][g[1]] == 'X':
                dg2[g][gg] += 1000000 - 2
        for i in range(min(g[1], gg[1]), max(g[1], gg[1])):
            if grid[g[0]][i] == 'X':
                dg2[g][gg] += 1000000 - 2
            
part1 = sum(sum(dg1[g].values()) for g in dg1)
part2 = sum(sum(dg2[g].values()) for g in dg2)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
