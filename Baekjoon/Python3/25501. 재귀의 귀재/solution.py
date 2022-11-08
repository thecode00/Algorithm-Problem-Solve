# https://www.acmicpc.net/problem/25501

import sys

input = sys.stdin.readline


def recursion(s, left, right):
    recur = 1
    if left >= right:
        return [1, 1]
    elif s[left] != s[right]:
        return [0, 1]
    else:
        info_list = recursion(s, left + 1, right - 1)
        info_list[1] += recur
        return info_list


for _ in range(int(input())):
    string = input().strip()
    print(" ".join(map(str, recursion(string, 0, len(string) - 1))))

###################################################################################

import sys

input = sys.stdin.readline


def recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


for _ in range(int(input())):
    string = input().strip()
    count = 0
    print(recursion(string, 0, len(string) - 1), count)
