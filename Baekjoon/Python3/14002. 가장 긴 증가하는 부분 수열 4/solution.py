"""
https://www.acmicpc.net/problem/14002
Time Complexity: O(N²)
"""


import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
dp = [1 for _ in range(n)]
max_index, max_length = 0, 1  # 가장 긴 증가 수열의 끝 인덱스, 길이

for idx in range(n):
    for i in range(idx):
        if sequence[idx] > sequence[i]:
            dp[idx] = max(dp[idx], dp[i] + 1)
    if dp[idx] > max_length:  # dp가 현재 최대길이 보다 길때 길이 갱신
        max_index = idx
        max_length += 1
print(dp[max_index])

answer = []
for idx in range(n - 1, -1, -1):
    # dp를 역으로 보면서 현재 최대길이와 같은 dp인덱스를 찾아서 값들을 가져옴
    if dp[idx] == max_length:
        answer.append(sequence[idx])
        max_length -= 1

# 길이가 긴 순서부터 리스트에 넣었기때문에 pop으로 가장 나중에 들어온 짧은값들을 출력
for _ in range(dp[max_index]):
    print(answer.pop(), end=" ")
