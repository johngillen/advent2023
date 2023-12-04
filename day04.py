import re

f = open('input/day04.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 0
part2 = 0

e = [0] * len(lines)
s = [1] * len(lines)

for i, line in enumerate(lines):
    c, w = line.split('|')
    c = [int(m) for m in re.findall(r'\d+', c)][1:]
    w = [int(m) for m in re.findall(r'\d+', w)]

    p = 0
    for n in c:
        if n in w:
            e[i] += 1
            p = p * 2 if p else 1
    part1 += p

for i in range(len(s)):
    for w in range(e[i]):
        s[i + w + 1] += s[i]
part2 = sum(s)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
