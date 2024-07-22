# https://codeforces.com/problemset/problem/1992/D

# DP
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    river = input().rstrip()

    # left bank(1) + river(n) + rignt bank(1)
    dp = [float("inf")] * (n + 2)
    dp[0] = 0

    for idx in range(1, n + 2):
        if idx != (n + 1) and river[idx - 1] == "C":
            continue

        for i in range(idx - m, idx):
            if i >= 0 and (i == 0 or river[i - 1] == "L"):
                dp[idx] = min(dp[idx], dp[i])

        if idx > 1 and river[idx - 2] == "W":
            dp[idx] = min(dp[idx], dp[idx - 1] + 1)
    if dp[-1] > k:
        print("NO")
    else:
        print("YES")


# TODO: Greedy
