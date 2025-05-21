"""
https://codeforces.com/problemset/problem/230/B
Time Complexity: O(N)
"""
from math import isqrt
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

max_range = 10 ** 6
primes = [True] * (max_range + 1)
primes[0] = primes[1] = False

for i in range(2, isqrt(max_range) + 1):
    if primes[i]:
        for j in range(i * i, max_range + 1, i):
            primes[j] = False

for num in numbers:
    root = isqrt(num)
    if root * root == num and primes[root]:
        print("YES")
    else:
        print("NO")
