# https://codeforces.com/problemset/problem/1132/B

n = int(input())
prices = list(map(int, input().split()))
m = int(input())

prices.sort()

queries = list(map(int, input().split()))

total = sum(prices)
for index in queries:
    print(total - prices[-index])
