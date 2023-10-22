"""
https://codeforces.com/problemset/problem/489/C
Time Complexity: O(N)
"""

import sys

input = sys.stdin.readline

m, s = map(int, input().split())
s2 = s
min_number, max_number = "", ""

if (m > 1 and s == 0) or s > m * 9:
    print("-1 -1")
else:

    def can(m, s):
        return s >= 0 and m * 9 >= s

    for idx in range(m):  # Find min number
        for num in range(10):
            if can(m - idx - 1, s - num):
                # When m is greater than 1 prevents the first digit being 0
                if idx == 0 and num == 0 and m > 1:
                    continue
                s -= num
                min_number += str(num)
                break

    for idx in range(m):  # Find max number
        for num in range(9, -1, -1):
            if can(m - idx - 1, s2 - num):
                s2 -= num
                max_number += str(num)
                break
    print(min_number, max_number)
