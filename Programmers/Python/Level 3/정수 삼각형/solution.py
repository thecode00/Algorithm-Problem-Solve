# https://school.programmers.co.kr/learn/courses/30/lessons/43105


# DP 탑 바텀 방식
def solution(triangle):
    length = len(triangle)
    # 삼각형의 길이 - 1번째 줄부터 첫번째줄까지 탑 바텀형식으로 내려감
    for idx in range(length - 2, -1, -1):
        for i in range(idx + 1):
            # 현재 줄의 윗줄에서 대각선 방향원소들중 가장 큰 원소를 더함
            triangle[idx][i] += max(triangle[idx + 1][i], triangle[idx + 1][i + 1])
    return triangle[0][0]
