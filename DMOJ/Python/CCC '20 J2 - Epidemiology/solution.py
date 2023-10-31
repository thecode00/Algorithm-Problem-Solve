# https://dmoj.ca/problem/ccc20j2

import sys

input = sys.stdin.readline

people = int(input())
patient = n = int(input())
r = int(input())
day = 0

while patient <= people:
    day += 1
    n *= r
    patient += n

print(day)
