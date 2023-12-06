import re

f = open('input/day06.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 1
part2 = 0

lt = [int(x) for x in re.findall(r'\d+', lines[0])]
ld = [int(x) for x in re.findall(r'\d+', lines[1])]

tt = int(''.join(str(i) for i in lt))
td = int(''.join(str(i) for i in ld))

for t, d, in zip(lt, ld):
    dd = 0
    for s in range(t):
        if s * (t - s) > d: dd += 1
    part1 *= dd

for s in range(tt):
    if s * (tt - s) > td: part2 += 1

print(f'part 1: {part1}')
print(f'part 2: {part2}')
