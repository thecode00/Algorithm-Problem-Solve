# https://www.acmicpc.net/problem/27433

import sys

input = sys.stdin.readline

n = int(input())


def factorial(num):
    if num <= 1:
        return 1

    return factorial(num - 1) * num


print(factorial(n))
