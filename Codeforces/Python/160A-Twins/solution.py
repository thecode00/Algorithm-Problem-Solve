# https://codeforces.com/problemset/problem/160/A

n = int(input())
coins = list(map(int, input().split()))
total = sum(coins)
coins.sort(reverse=True)

my_coin = 0
for idx, coin in enumerate(coins):
    my_coin += coin
    total -= coin
    if total < my_coin:
        print(idx + 1)
        break
