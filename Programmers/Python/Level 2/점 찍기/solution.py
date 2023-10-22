# https://school.programmers.co.kr/learn/courses/30/lessons/140107

def solution(k, d):
    count = 0
    # 최대거리
    max_dist = d ** 2
    for x in range(0, d + 1, k):
        # 거리공식 (x ^ 2 + y ^ 2) ** .5에서 x가 정해졌으니 y의 최대좌표를 구함
        cur_max_point = int((max_dist - (x ** 2)) ** .5)
        # 좌표는 y * k형식으로 늘어나므로 k로 나눠서 1 ~ y까지 k가 몇개들어가는지 구하고 y == 0일때를 추가하기 위해 1을더함
        count += cur_max_point // k + 1
    return count
