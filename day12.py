from functools import cache

f = open('input/day12.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 0
part2 = 0

@cache
def f(s, g, li):
    if not s:
        if (not g and not li) or tuple([g]) == li: return 1
        return 0
    
    if (g and not li) or g + sum([1 for c in s if c in '#?']) < sum(li): return 0

    p = 0
    if s[0] in '.?' and g and g == li[0]: p += f(s[1:], 0, li[1:])
    if s[0] in '.?' and not g: p += f(s[1:], 0, li)
    if s[0] in '#?': p += f(s[1:], g + 1, li)
    return p

for line in lines:
    s, li = line.split()
    li = tuple([int(i) for i in li.split(',')])

    part1 += f(s, 0, li)
    part2 += f('?'.join([s] * 5), 0, li * 5)
    
print(f'part 1: {part1}')
print(f'part 2: {part2}')
