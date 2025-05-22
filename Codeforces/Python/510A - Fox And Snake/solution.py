# https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().split())
right_turn = True

for row in range(n):
    if row % 2 == 0:
        print("#" * m)
    else:
        print(f"{'#' * (not right_turn)}{'.' * (m - 1)}{'#' * right_turn}")
        right_turn = not right_turn
