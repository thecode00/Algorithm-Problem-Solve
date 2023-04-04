# https://school.programmers.co.kr/learn/courses/30/lessons/12914


def solution(n):
    if n <= 2:
        return n
    dp = [0 for _ in range(n + 1)]
    dp[1], dp[2] = 1, 2
    for idx in range(3, n + 1):
        dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 1234567
    return dp[n]


print(solution(4))
