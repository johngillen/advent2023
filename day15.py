import re

f = open('input/day15.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 0
part2 = 0

lt = lines[0].split(',')
lb = [[] for _ in range(256)]

def f(s):
    n = 0
    for c in s:
        n += ord(c)
        n *= 17
        n %= 256
    return n

for t in lt:
    part1 += f(t)

    l, o, v = re.match(r'(\w+)([-=]{1})(\d?)', t).groups()
    if v: v = int(v)

    if o == '-':

        if l in [lv[0] for lv in lb[f(l)]]:
            for i, lv in enumerate(lb[f(l)]):
                if lv[0] == l: lb[f(l)].pop(i)
    else:
        if l in [lv[0] for lv in lb[f(l)]]:
            for i, lv in enumerate(lb[f(l)]):
                if lv[0] == l: lb[f(l)][i] = (l, v)
        else: lb[f(l)].append((l, v))

for i, b in enumerate(lb):
    for j, lv in enumerate(b):
        part2 += (i + 1) * (j + 1) * int(lv[1])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
