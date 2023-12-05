import re

f = open('input/day05.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 0
part2 = 0

ls, ls2 = [int(n) for n in re.findall(r'\d+', lines[0])], []
lm = [[] for _ in range(7)]
im = iter(lm)

for line in lines[1:]:
    if not any(line): m = next(im)
    if any(c.isdigit() for c in line):
        m.append([int(n) for n in re.findall(r'\d+', line)])

def f(s, im=None):
    if im is None: im = iter(lm)
    try: m = next(im)
    except: return s
    for r in m:
        ro, ri, rs = r
        if ri <= s < ri + rs:
            return f(ro + s - ri, im)
        elif r == m[-1]:
            return f(s, im)

part1 = min([f(s) for s in ls])

for i, j in list(zip(ls[::2], ls[1::2])):
    ls2 += list(range(i, i + j, 10000))
ls2 = min(ls2, key=f)
part2 = min(f(s) for s in range(ls2 - 10000, ls2 + 10000))

print(f'part 1: {part1}')
print(f'part 2: {part2}')
