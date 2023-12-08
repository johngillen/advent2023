import re
import itertools
from math import gcd

f = open('input/day08.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 0
part2 = 0

ld = lines[0]
nm = {}

for line in lines[2:]:
    n, l, r = [m for m in re.findall(r'\w{3}', line)]
    nm[n] = (l, r)

def dist(s, e):
    x = 0
    cd = itertools.cycle(ld)
    while not s.endswith(e):
        d = next(cd)
        l, r = nm[s]
        s = l if d == 'L' else r
        x += 1
    return x

def lcm(l):
    x = 1
    for i in l:
        x = x * i // gcd(x, i)
    return x

part1 = dist('AAA', 'ZZZ')
part2 = lcm([dist(n, 'Z') for n in nm.keys() if n.endswith('A')])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
