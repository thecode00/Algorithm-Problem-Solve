# https://codeforces.com/problemset/problem/263/A

matrix = []

for _ in range(5):
    matrix.append(list(map(int, input().split())))

for row in range(5):
    for col in range(5):
        if matrix[row][col]:
            print(abs(row - 2) + abs(col - 2))
