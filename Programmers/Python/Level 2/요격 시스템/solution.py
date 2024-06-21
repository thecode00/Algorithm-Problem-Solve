# https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    targets.sort(key=lambda x: (x[1]))

    shoot_range = []

    for start, end in targets:
        # 미사일이 사격범위안에 들어오는지 확인
        if not shoot_range or start >= shoot_range[-1][1]:
            shoot_range.append([start, end])

    return len(shoot_range)
