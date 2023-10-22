# https://codeforces.com/problemset/problem/133/A

p = input()
for cmd in p:
    if cmd in ["Q", "H", "9"]:
        print("YES")
        break
else:
    print("NO")