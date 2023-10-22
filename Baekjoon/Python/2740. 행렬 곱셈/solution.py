# https://www.acmicpc.net/problem/2740


import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # 벡터 a의 크기
vector_a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())  # 벡터 b의 크기
vector_b = [list(map(int, input().split())) for _ in range(m)]
vector_c = [[0 for _ in range(k)] for _ in range(n)]  # 행렬곱으로 만들어진 새로운 벡터


def mul(y, x):
    # n * m, m * k 크기의 행렬곱의 결과는 m * m 벡터가 되므로 m을 가져옴
    global vector_a, vector_b, m
    num = 0

    for idx in range(m):
        num += vector_a[y][idx] * vector_b[idx][x]
    return num


for y in range(n):
    for x in range(k):
        vector_c[y][x] = mul(y, x)
    print(" ".join(map(str, vector_c[y])))
