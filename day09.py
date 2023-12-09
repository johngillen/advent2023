import re

f = open('input/day09.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 0
part2 = 0

for line in lines:
    ld = [[int(m) for m in re.findall(r'-?\d+', line)]]
    while any(e != 0 for e in ld[-1]):
        ld.append([a - b for a, b in zip(ld[-1][1:], ld[-1][:-1])])

    for i, d in reversed(list(enumerate(ld[1:]))):
        ld[i - 1] += [ld[i - 1][-1] + ld[i][-1]]
        ld[i - 1].insert(0, ld[i - 1][0] - ld[i][0])
       
    part1 += ld[0][-1]
    part2 += ld[0][0]

print(f'part 1: {part1}')
print(f'part 2: {part2}')
