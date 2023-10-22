# https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    dp = [0] * n
    dp[0], dp[1] = 1, 2
    for idx in range(2, n):
        # 타일로 만들수있는 최대크기가 2 * 2이므로 n - 2까지만 dp를 함
        # 설명을 쉽게 잘 하신분의 블로그: https://wwlee94.github.io/category/algorithm/dp/2xn-tiling/
        dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 1000000007
    return dp[n - 1]
