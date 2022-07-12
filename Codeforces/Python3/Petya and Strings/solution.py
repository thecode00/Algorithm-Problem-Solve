# https://codeforces.com/problemset/problem/112/A

first, second = input().lower(), input().lower()

for s1, s2 in zip(first, second):
    if s1 > s2:
        print(1)
        break
    elif s2 > s1:
        print(-1)
        break
else:   # When break does not executed in for loop
    print(0)
