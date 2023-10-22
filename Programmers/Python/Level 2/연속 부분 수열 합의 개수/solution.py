# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    size = len(elements)
    # dp[i][j] = 시작지점이 j이고 길이가 i인 부분수열의 합
    dp = [[0] * size for _ in range(size)]

    sums = set()
    for i in range(1, size):    # 부분수열의 길이
        for idx in range(size):
            # 길이가 i - 1인 부분수열에 elements[idx]를 추가한 길이가 i인 부분수열의 합 구함
            new_sum = dp[i - 1][idx - i] + elements[idx]
            dp[i][idx - i] = new_sum
            sums.add(new_sum)

    sums.add(sum(elements))
    # print(sums)
    return len(sums)
