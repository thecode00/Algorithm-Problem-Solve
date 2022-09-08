# https://codeforces.com/problemset/problem/131/A

import sys

input = sys.stdin.readline

string = input().strip()

if string[1:] == string[1:].upper():  #
    print(string.swapcase())
else:
    print(string)
