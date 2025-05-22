# https://codeforces.com/problemset/problem/691/A

n = int(input())
buttons = sum(map(int, input().split()))

if n == 1:
    print("YES" if buttons == 1 else "NO")
else:
    print("YES" if n - buttons == 1 else "NO")
