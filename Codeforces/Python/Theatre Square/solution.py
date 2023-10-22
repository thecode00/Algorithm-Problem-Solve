# https://codeforces.com/problemset/problem/1/A

n, m, a = map(int, input().split())
w = m // a if m % a == 0 else m // a + 1
h = n // a if n % a == 0 else n // a + 1
print(w * h)
