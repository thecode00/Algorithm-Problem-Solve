"""
https://www.acmicpc.net/problem/1699
Time Complexity: O(N)
"""


import sys

input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n + 1)]
dp[1] = 1

cur_square_num = 1  # 현재 완전제곱수의 제곱근
cur_square = 1  # 현재 완전제곱수
next_square = 4  # 다음 완전제곱수
for idx in range(2, n + 1):
    # print(idx, cur_square, next_square)
    if idx == next_square:
        # 현재 idx가 다음 완전제곱수라면 현재 완전제곱수를 다음 완전제곱수로 설정
        cur_square, next_square = next_square, (cur_square_num + 2) ** 2
        cur_square_num += 1
        dp[idx] = 1
    else:
        # 현재 가장 큰 완전제곱수를 뺀 나머지의 dp에서 값을 가져오면 됨
        dp[idx] = dp[idx - cur_square] + 1
print(dp[n])
