# https://codeforces.com/problemset/problem/266/A

n = int(input())
stones = input()
answer = 0
for idx in range(n - 1):
    if stones[idx] == stones[idx + 1]:
        answer += 1
print(answer)
