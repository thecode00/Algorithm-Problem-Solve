# https://www.acmicpc.net/problem/11729

n = int(input())

move = []


def hanoi(n, ori, temp, dest):
    if n == 1:
        move.append(f"{ori} {dest}")
        return

    hanoi(n - 1, ori, dest, temp)
    move.append(f"{ori} {dest}")
    hanoi(n - 1, temp, ori, dest)


hanoi(n, 1, 2, 3)

print(len(move))

for m in move:
    print(m)
