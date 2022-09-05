# https://codeforces.com/problemset/problem/479/A

import sys

input = sys.stdin.readline

a, b, c = int(input()), int(input()), int(input())
print(max((a+b)*c, a+b+c, a*(b+c), a*b*c))
