# https://school.programmers.co.kr/learn/courses/30/lessons/42884


def solution(routes):
    # 차량의 진출 지점순으로 정렬한다음 진출지점에 카메라를 설치한다면 진입지점이 카메라의 설치 지점보다 앞에있는 차량들의 진출지점이
    # 카메라가 설치되어있는 지점보다 뒤에 있는게 보장됨
    routes.sort(key=lambda x: x[1])
    camera = 0
    position = float("-inf")
    for start, end in routes:
        # 새로운 차가 기존의 카메라 감시지점에서 벗어날경우 카메라를 새로 추가
        if start > position:
            camera += 1
            position = end

    return camera
