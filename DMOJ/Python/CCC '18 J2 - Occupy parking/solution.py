# https://dmoj.ca/problem/ccc18j2

import sys

input = sys.stdin.readline

length = int(input())
yesterday = input().strip()
today = input().strip()
count = 0

for y_car, t_car in zip(yesterday, today):
    if y_car == t_car == "C":
        count += 1

print(count)
