# https://codeforces.com/problemset/problem/1167/A

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    phone_number = input().rstrip()
    eight_index = phone_number.find("8")

    if n < 11 or eight_index == -1:
        print("NO")
        continue

    if n - eight_index < 11:
        print("NO")
    else:
        print("YES")
