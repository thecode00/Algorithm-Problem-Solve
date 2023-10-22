"""
https://codeforces.com/problemset/problem/456/A
Time complexity: O(N)
"""

import sys

input = sys.stdin.readline

# My answer
laptops = []
amount = int(input())
for _ in range(amount):
    laptops.append(list(map(int, input().split())))  # [price, quality]
laptops.sort(key=lambda x: (x[0], -x[1]))
for idx in range(1, amount):
    if laptops[idx][1] < laptops[idx - 1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")

# Problem provider answer
# Maybe problem has error?
# When [10, 8], [5, 4] they should print "Poor Alex"
for _ in range(int(input())):
    price, quality = map(int, input().split())
    if price != quality:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
