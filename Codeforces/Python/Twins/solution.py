# https://codeforces.com/problemset/problem/160/A

n = int(input())
coins = list(map(int, input().split()))
total = sum(coins)
coins.sort(reverse=True)
for idx in range(1, n):
    coins[idx] += coins[idx - 1]
# print(coins)
for idx in range(n):
    # coins[idx] = sum of my coins, total - coins[idx] = sum on twin coins
    if total - coins[idx] < coins[idx]:
        print(idx + 1)
        break
