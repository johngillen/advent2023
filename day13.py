f = open('input/day13.txt')
groups = [g.split() for g in f.read().split('\n\n')]
              
part1 = 0
part2 = 0

def d(a, b):
    return sum(sum(ac != bc for ac, bc in zip(al, bl)) for al, bl in zip(a, b))

def r(g, n):
    for i in range(1, len(g)):
        a, b = g[:i], g[i:]
        if d(a[::-1], b) == n:
            return i
    return 0

for group in groups:
    part1 += 100 * r(group, 0)
    part1 += r(list(zip(*group[::-1])), 0)
    part2 += 100 * r(group, 1)
    part2 += r(list(zip(*group[::-1])), 1)
    
print(f'part 1: {part1}')
print(f'part 2: {part2}')
