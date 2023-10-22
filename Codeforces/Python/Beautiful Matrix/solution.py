# https://codeforces.com/problemset/problem/263/A

matrix = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            print(abs(i - 2) + abs(j - 2))  # Middle point = (2, 2)
