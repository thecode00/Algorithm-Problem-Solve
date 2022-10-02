"""
https://codeforces.com/problemset/problem/25/A
Time complexity: O(N)
"""

import sys

input = sys.stdin.readline

n = int(input())
evenness = list(map(int, input().split()))
even, odd = 0, 0
for num in evenness:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
# Use bruteforce
if even == 1:
    for idx, num in enumerate(evenness):
        if num % 2 != 0:
            print(idx + 1)
else:
    for idx, num in enumerate(evenness):
        if num % 2 == 0:
            print(idx + 1)
