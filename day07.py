from functools import cmp_to_key

f = open('input/day07.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

r1 = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
r2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

hb = [(h, int(b)) for h, b in [line.split(' ') for line in lines]]

def s(h):
    if any([h.count(c) == 5 for c in h]):
        return 5
    if any([h.count(c) == 4 for c in h]):
        return 4
    if any([h.count(c) == 3 for c in h]) and \
       any([h.count(c) == 2 for c in h]):
        return 3
    if any([h.count(c) == 3 for c in h]):
        return 2
    if len([c for c in set(h) if h.count(c) == 2]) == 2:
        return 1
    if any([h.count(c) == 2 for c in h]):
        return 0
    return -1

def ch(a, b):
    a, b = a[0], b[0]

    sa, sb = s(a), s(b)

    if sa > sb: return 1
    if sa < sb: return -1
    
    for ca, cb in zip(a, b):
        if r1.index(ca) > r1.index(cb):
            return 1
        if r1.index(ca) < r1.index(cb):
            return -1

def cw(a, b):
    a, b = a[0], b[0]

    sa = max(s(a.replace(ca, 'J')) for ca in set(a))
    sb = max(s(b.replace(ba, 'J')) for ba in set(b))

    if sa > sb: return 1
    if sa < sb: return -1
    
    for ca, cb in zip(a, b):
        if r2.index(ca) > r2.index(cb):
            return 1
        if r2.index(ca) < r2.index(cb):
            return -1

part1 = sum([(i + 1) * p[1] for i, p in enumerate(sorted(hb, key=cmp_to_key(ch)))])
part2 = sum([(i + 1) * p[1] for i, p in enumerate(sorted(hb, key=cmp_to_key(cw)))])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
