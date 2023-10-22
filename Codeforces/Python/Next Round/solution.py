# https://codeforces.com/problemset/problem/158/A

# O(n)
n, k = map(int, input().split())
ranking = list(map(int, input().split()))
k_score = ranking[k - 1]
answer = 0
for score in ranking:
    if score >= k_score and score > 0:
        answer += 1
    else:
        break
print(answer)
