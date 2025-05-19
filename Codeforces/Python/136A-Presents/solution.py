# https://codeforces.com/problemset/problem/136/A

n = int(input())
give = list(map(int, input().split()))

receive = [0] * n

for idx, give_num in enumerate(give):
    receive[give_num - 1] = idx + 1

print(*receive)
