# https://codeforces.com/problemset/problem/1702/D

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    w = list(input().rstrip())
    length = len(w)
    p = int(input())
    list_ord = [ord(s) - 96 for s in w]
    list_ord.sort()
    check = length  # Initialize to max value
    for idx in range(length):
        p -= list_ord[idx]
        if p < 0:
            check = idx
            break
    dict_chr = {chr(x): 0 for x in range(97, 123)}   # All of lower alphabet
    for idx in range(check):
        dict_chr[chr(list_ord[idx] + 96)] += 1
    # print(dict_chr)
    answer = ""
    for s in w:
        if dict_chr[s] != 0:
            answer += s
            dict_chr[s] -= 1
    print(answer)
