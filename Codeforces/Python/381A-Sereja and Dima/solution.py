# https://codeforces.com/problemset/problem/381/A

n = int(input())

cards = list(map(int, input().split()))

left = 0
right = n - 1
scores = [0, 0]
turn = 0

while left < right:
    if cards[left] < cards[right]:
        scores[turn] += cards[right]
        right -= 1
    else:
        scores[turn] += cards[left]
        left += 1

    turn ^= 1

    if cards[left] < cards[right]:
        scores[turn] += cards[right]
        right -= 1
    else:
        scores[turn] += cards[left]
        left += 1

    turn ^= 1

if left == right:
    scores[turn] += cards[left]

print(*scores)
