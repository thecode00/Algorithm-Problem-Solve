# https://www.acmicpc.net/problem/11052


import sys

input = sys.stdin.readline

n = int(input())  # 카드 구매 개수
price = list(map(int, input().split()))  # 카드 가격
# dp[n]은 n개의 카드를살때 가장 비싼 가격
dp = [0 for _ in range(n + 1)]

for idx in range(1, n + 1):
    for i in range(1, idx + 1):
        # 3개가 든 카드팩을 샀을때
        dp[idx] = max(dp[idx], dp[idx - i] + price[i - 1])
print(dp[n])
