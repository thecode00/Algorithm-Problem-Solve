# https://codeforces.com/problemset/problem/492/B

import sys

input = sys.stdin.readline

n, l = map(int, input().split())
lanterns = list(map(int, input().split()))
lanterns.sort()

max_lantern_dist = 0
for idx in range(n - 1):
    max_lantern_dist = max(max_lantern_dist, lanterns[idx + 1] - lanterns[idx])
# Check distance between max lanterns distance, first lantern and 0, last lantern and l
print(max(max_lantern_dist / 2, lanterns[0], l - lanterns[-1]))
