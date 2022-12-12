# https://www.acmicpc.net/problem/1912


import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
dp = [num for num in numbers]

for idx in range(1, n):
    # dp[idx - 1]까지의 연속합에 현재값을 더하는게 손해일경우 연속합을 끊고 dp[idx]에 현재값을 할당
    if dp[idx] < dp[idx - 1] + numbers[idx]:
        dp[idx] = dp[idx - 1] + numbers[idx]
print(max(dp))
