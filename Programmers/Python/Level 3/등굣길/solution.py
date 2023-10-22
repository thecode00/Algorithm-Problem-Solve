# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    dp = [[1] * m for _ in range(n)]

    # 물웅덩이 처리
    for x, y in puddles:
        # 좌표가 0 베이스 넘버링이 아니기 떄문에 0 베이스로 변환
        x, y = x - 1, y - 1
        if dp[y][x] == 0:
            continue
        # 물웅덩이가 x = 0에 생기면 아래로 갈수있는 경로를 막고 y = 0에 생기면 오른쪽으로 갈수있는 경로를 막음
        if x == 0:
            for idx in range(y, n):
                dp[idx][x] = 0
        elif y == 0:
            for idx in range(x, m):
                dp[y][idx] = 0
        else:
            dp[y][x] = 0

    for y in range(1, n):
        for x in range(1, m):
            if dp[y][x] == 0:   # 물 웅덩이는 무시
                continue
            dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % 1000000007

    return dp[-1][-1]
