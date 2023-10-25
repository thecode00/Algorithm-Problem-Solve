# https://dmoj.ca/problem/coci16c1p1

import sys

input = sys.stdin.readline

x = int(input())
data = 0
# Input data usage for each month and subtract it from the total data.
for _ in range(int(input())):
    current_month_spend = int(input())
    data += x - current_month_spend

print(data + x)
