f = open('input/day14.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

grid = [[c for c in line] for line in lines]

def l():
    n = 0
    for x, r in enumerate(grid):
        for c in r:
            if c == 'O': n += len(grid) - x
    return n

def f():
    global grid
    while True:
        fl = True
        for x, r in enumerate(grid[:-1]):
            for y, c in enumerate(r):
                if c == '.' and grid[x + 1][y] == 'O':
                    grid[x + 1][y], grid[x][y] = '.', 'O'
                    fl = False
        if fl: break

def c():
    global grid
    for _ in range(4):
        f()
        grid = [list(row) for row in list(zip(*grid[::-1]))]

f()
part1 = l()

seen = []
for i in range(1000000000):
    h = hash(str(grid))
    if h in seen:
        for _ in range((1000000000 - i) % (i - seen.index(h))):
            c()
        break
    seen += [h]
    c()
part2 = l()

print(f'part 1: {part1}')
print(f'part 2: {part2}')
