# https://codeforces.com/problemset/problem/282/A
import sys
input = sys.stdin.readline

X = 0
for _ in range(int(input())):
    oper = input().strip()
    if "+" in oper:
        X += 1
    else:
        X -= 1
print(X)
