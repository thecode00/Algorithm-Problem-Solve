
import sys

input = sys.stdin.readline

n = int(input())
num = 0

for _ in range(n):
    oper = list(input().rstrip())

    if oper[1] == "+":
        num += 1
    else:
        num -= 1

print(num)
