# https://www.acmicpc.net/problem/11053


from bisect import bisect_left
import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))

# Bruteforce: O(N²)
dp = [1 for _ in range(n)]
for idx in range(1, n):
    for i in range(idx):
        if sequence[idx] > sequence[i]:
            dp[idx] = max(dp[idx], dp[i] + 1)
print(max(dp))

# Binary search: O(N log N)
dp = [sequence[0]]
for idx in range(1, n):
    if sequence[idx] > dp[-1]:
        dp.append(sequence[idx])
    else:
        dp[bisect_left(dp, sequence[idx])] = sequence[idx]
print(len(dp))
