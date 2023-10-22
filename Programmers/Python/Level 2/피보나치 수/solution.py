# https://school.programmers.co.kr/learn/courses/30/lessons/12945


def solution(n):
    if n < 2:
        return n
    dp = [0, 1]
    for idx in range(2, n + 1):
        dp.append((dp[idx - 1] + dp[idx - 2]) % 1234567)
    return dp[n]
