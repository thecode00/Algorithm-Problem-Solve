# https://codeforces.com/problemset/problem/1000/A

from collections import defaultdict


n = int(input())

previous = defaultdict(int)
current = defaultdict(int)

for _ in range(n):
    size = input()
    previous[size] += 1

for _ in range(n):
    size = input()
    current[size] += 1

diff = 0

for size, count in current.items():
    if previous[size] >= count:
        continue

    diff += count - previous[size]

print(diff)
