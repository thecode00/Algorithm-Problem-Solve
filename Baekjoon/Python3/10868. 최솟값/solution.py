# https://www.acmicpc.net/problem/10868


import sys

input = sys.stdin.readline

n, m = map(int, input().split())    # 정수 개수, 숫자 쌍 개수
arr = []
for _ in range(n):
    arr.append(int(input()))

height = [0 for _ in range(n + 1)]
for i in range(2, n + 1):
    height[i] = height[i >> 1] + 1


# table의 y는 구하고싶은 범위의 인덱스 i까지 2의 몇승인지 나타냄 x는 x ~ x + (2 ^ y)까지의 최소값을 저장
# y가 0이면 2 ^ y = 2 ^ 0 = 1이므로 범위가 x ~ x의 최소값을 저장한다 그러므로 y = 0에는 배열의 원소만 저장
# 만약 table[0][i]면 arr의 i부터 2 ^ 0개까지의 최소값을 저장함, table[i][j]라면 j부터 2 ^ i개의 원소중 최소값을 저장
table = [[-1 for _ in range(n)] for _ in range(height[-1] + 1)]
table[0] = arr


step = 1
for i in range(1, len(table)):
    for j in range(n):
        if j + step < n:
            table[i][j] = min(table[i-1][j], table[i - 1][j + step])
    step <<= 1   # y가 커질수록 범위가 2의 제곱으로 커지기때문에 비트시프트로 2를 곱해줌

for _ in range(m):
    a, b = map(int, input().split())
    # 0-index로 바꿈
    a -= 1
    b -= 1
    row = height[b - a + 1]  # a와 b까지의 거리
    print(min(table[row][a], table[row][b + 1 - (1 << row)])) 

# 테스트용
print(height)
print(table)
