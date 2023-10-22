# https://www.acmicpc.net/problem/14888


import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
oper = list(map(int, input().split()))

# 재귀방식
def max_calc(num, idx, opers):
    if idx == n:
        return num
    max_value = -float("inf")
    for i in range(4):
        if opers[i] != 0:
            opers[i] -= 1
            if i == 0:
                max_value = max(max_value, max_calc(num + numbers[idx], idx + 1, opers))
            elif i == 1:
                max_value = max(max_value, max_calc(num - numbers[idx], idx + 1, opers))
            elif i == 2:
                max_value = max(max_value, max_calc(num * numbers[idx], idx + 1, opers))
            else:
                max_value = max(max_value, max_calc(int(num / numbers[idx]), idx + 1, opers))
            opers[i] += 1
    return max_value


def min_calc(num, idx, opers):
    if idx == n:
        return num
    min_value = float("inf")
    for i in range(4):
        if opers[i] != 0:
            opers[i] -= 1
            if i == 0:
                min_value = min(min_value, min_calc(num + numbers[idx], idx + 1, opers))
            elif i == 1:
                min_value = min(min_value, min_calc(num - numbers[idx], idx + 1, opers))
            elif i == 2:
                min_value = min(min_value, min_calc(num * numbers[idx], idx + 1, opers))
            else:
                min_value = min(min_value, min_calc(int(num / numbers[idx]), idx + 1, opers))
            opers[i] += 1
    return min_value


print(max_calc(numbers[0], 1, oper))
print(min_calc(numbers[0], 1, oper))
