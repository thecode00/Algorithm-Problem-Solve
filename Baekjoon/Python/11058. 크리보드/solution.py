# https://www.acmicpc.net/problem/11058


import sys

input = sys.stdin.readline

n = int(input())
# 복사를 하지않고 타이핑만 한 경우의 수
dp = [num for num in range(n + 1)]

"""
복사에 3턴이상이 걸리므로 3이상부터 복사체크를 함
한번 붙여넣으면 계속 복사할수있다는것을 잊지말아야 함
"""
for idx in range(3, n + 1):
    for i in range(3, idx + 1):
        """
        3번째전것을 복사한경우: dp[idx - 3] * 2
        4번째전것을 복사한경우: dp[idx - 4] * 3
        점화식: dp[idx - i] * (i - 1)
        """
        dp[idx] = max(dp[idx], dp[idx - i] * (i - 1))
print(dp[n])
