"""
https://codeforces.com/problemset/problem/230/B
Time Complexity: O(N)
TODO: problem solve
"""

from math import sqrt
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

for num in numbers:
    """
    If it is a square number, the number of factors is odd,
    Ex. 4 == 2 ^ 2, factor: 1, 2, 4   9 == 3 ^ 2, factor: 1, 3, 9
    """
    if int(sqrt(num)) ** 2 == num and num != 1:
        print("YES")
    else:
        print("NO")
