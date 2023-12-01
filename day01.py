f = open('input/day01.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

l = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for line in lines:
	n = [c for c in line if c.isdigit()]
	part1 += int(n[0] + n[-1])

	lo = min([(line.find(e), e) for e in l if line.find(e) != -1])
	hi = max([(line.rfind(e), e) for e in l if line.rfind(e) != -1])

	if lo[1] in l[:9]: lo = (lo[0], l[l.index(lo[1]) + 9])
	if hi[1] in l[:9]: hi = (hi[0], l[l.index(hi[1]) + 9])

	part2 += int(lo[1] + hi[1])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
