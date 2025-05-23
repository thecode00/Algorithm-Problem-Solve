# https://codeforces.com/problemset/problem/279/B

n, t = map(int, input().split())
books = list(map(int, input().split()))

left = 0
max_books = 0
times = 0

for right in range(n):
    times += books[right]

    while left <= right and times > t:
        times -= books[left]
        left += 1

    max_books = max(max_books, right - left + 1)

print(max_books)
