# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):  # 최대트럭수용개수, 최대무게, 트럭들
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)    # 다리 구현
    total = 0   # 현재 다리위에있는 트럭의 무게 총합
    # 대기중인 트럭이없을때 데이터 추가없이 계속 popleft만 실행하기때문에 bridge의 길이가 0일때 모든 트럭이 다 건넌것
    while bridge:
        total -= bridge.popleft()    # 이동 구현
        if truck_weights:
            # 여기서 total대신 sum을 사용하면 sum의 시간복잡도가 O(N)이기 때문에 매우느림
            if total + truck_weights[0] <= weight:
                temp = truck_weights.popleft()
                bridge.append(temp)
                total += temp
            else:
                bridge.append(0)
        answer += 1
    return answer
