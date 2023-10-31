# https://dmoj.ca/problem/ccc18s1

import sys

input = sys.stdin.readline

towns = [int(input()) for _ in range(int(input()))]
towns.sort()
size = float("inf")
for idx in range(1, len(towns) - 1):
    # Comparing the previous minimum town size with the current town size
    size = min(size, (towns[idx + 1] - towns[idx - 1]) / 2)

print(size)
