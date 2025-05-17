
n, t = map(int, input().split())
queue = list(input())

for _ in range(t):
    idx = 0
    while idx < n - 1:
        if queue[idx] == "B" and queue[idx + 1] == "G":
            queue[idx], queue[idx + 1] = queue[idx + 1], queue[idx]
            idx += 1
        idx += 1

print("".join(queue))
