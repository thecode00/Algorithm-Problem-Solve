"""
https://codeforces.com/problemset/problem/1352/C
Time complexity: O(1)
"""

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    """
    Ex. n = 3, k = 7
    not divisible by n numbers will be: 1, 2 | 4, 5 | 7, 8 | 10, 11...
    they grouped n - 1, so divide n - 1 to find the group    ^ 4th group, first index
    and use the remainder to find the index
    """
    quot, remain = k // (n - 1), k % (n - 1)
    print(n * quot + remain if remain != 0 else n * quot - 1)
