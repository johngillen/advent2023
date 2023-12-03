f = open('input/day01.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

d = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', \
     '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}

for line in lines:
    n = [c for c in line if c.isdigit()]
    part1 += int(n[0] + n[-1])

    lo = min([[line.find(e), e] for e in d.keys() if line.find(e) != -1])
    hi = max([[line.rfind(e), e] for e in d.keys() if line.rfind(e) != -1])

    part2 += int(d[lo[1]] + d[hi[1]])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
