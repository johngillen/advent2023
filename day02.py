f = open('input/day02.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 0
part2 = 0

d1 = {'r': 12, 'g': 13, 'b': 14}
d2 = {'r': 0, 'g': 0, 'b': 0}

for i, line in enumerate(lines):
    _, line = line.split(': ')
    line = line.split('; ')
    v = True
    d2 = {'r': 0, 'g': 0, 'b': 0}
    for s in line:
        p = [(c[0], int(n)) for n, c in [x.split(' ') for x in s.split(', ')]]
        for c, n in p:
            if n > d1[c]: v = False; break
        for c, n in p:
            d2[c] = max(d2[c], n)
    if v: part1 += i + 1
    part2 += d2['r'] * d2['g'] * d2['b']

print(f'part 1: {part1}')
print(f'part 2: {part2}')
