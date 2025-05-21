# https://codeforces.com/problemset/problem/706/B

from bisect import bisect_right
import sys

input = sys.stdin.readline

n = int(input())
shops = list(map(int, input().split()))
shops.sort()
for _ in range(int(input())):
    # Bisect library is way to easy use binary search so use bisect library
    pos = bisect_right(shops, int(input()))
    sys.stdout.write(str(pos) + "\n")
