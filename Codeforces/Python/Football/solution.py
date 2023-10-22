# https://codeforces.com/problemset/problem/96/A

player = list(input())
number = 1
cur_team = "0"
for p in player:
    if p == cur_team:
        number += 1
    else:
        number = 1
        cur_team = p
    if number >= 7:
        print("YES")
        break
else:
    print("NO")
