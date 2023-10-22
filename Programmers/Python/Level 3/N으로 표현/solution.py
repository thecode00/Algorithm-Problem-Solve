# https://school.programmers.co.kr/learn/courses/30/lessons/42895


def solution(N, number):
    dp = [set() for _ in range(9)]  # 최소값이 8보다 크면 -1을 출력하므로 8까지만 계산
    for idx in range(1, 9):
        dp[idx].add(int(f"{N}" * idx))
        for j in range(idx):
            """
            숫자를 4개 쓴 경우를 볼때
            (dp[1], dp[3]), (dp[3], dp[1])만 탐색하지말고
            dp[2], dp[2]인 경우도 탐색해야한다
            """
            for k in dp[j]:
                for n in dp[idx - j]:
                    dp[idx].update([k + n, k - n, k * n])
                    if n != 0:
                        dp[idx].add(k // n)
        if number in dp[idx]:
            return idx
    else:
        return -1


# Test
solution(5, 12)
solution(2, 11)
solution(1, 1)
