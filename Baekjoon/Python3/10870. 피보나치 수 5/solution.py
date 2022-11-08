# https://www.acmicpc.net/problem/10870

n = int(input())
dp = [0, 1]
if n in dp:
    print(n)
else:
    dp += [0] * (n - 1)
    for idx in range(2, n + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]
    print(dp[n])
