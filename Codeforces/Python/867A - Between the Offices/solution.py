# https://codeforces.com/problemset/problem/867/A

n = int(input())
city = input()

s_to_f = 0
f_to_s = 0

for idx in range(n - 1):
    if city[idx] != city[idx + 1]:
        if city[idx] == "S":
            s_to_f += 1
        else:
            f_to_s += 1

print("YES" if s_to_f > f_to_s else "NO")
