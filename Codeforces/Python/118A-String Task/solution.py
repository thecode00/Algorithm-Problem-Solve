# https://codeforces.com/problemset/problem/118/A

import sys

input = sys.stdin.readline
print = sys.stdout.write

string = input().strip().lower()
vowels = set(["a", "o", "y", "e", "u", "i"])
for s in string:
    if s not in vowels:
        print("." + s)
