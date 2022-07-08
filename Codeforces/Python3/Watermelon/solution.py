# https://codeforces.com/problemset/problem/4/A

w = int(input())
answer = "YES" if w % 2 == 0 and w > 2 else "NO"    # If watermelon weight == 2
print(answer)
