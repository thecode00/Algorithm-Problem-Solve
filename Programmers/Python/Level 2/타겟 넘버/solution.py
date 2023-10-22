# https://programmers.co.kr/learn/courses/30/lessons/43165
from collections import deque


def solution(numbers, target):
    answer = 0
    length = len(numbers)
    q = deque()
    q.append([numbers[0], 0])
    q.append([-numbers[0], 0])
    while q:
        now, idx = q.popleft()
        idx += 1
        if idx < length:    # 큐에 다음인덱스의 숫자를 더하거나 뺀값을 추가
            q.append([now + numbers[idx], idx])
            q.append([now - numbers[idx], idx])
        else:
            if now == target:   # 모든 숫자를 다 더했을때 타겟값이 된 경우
                answer += 1
    return answer
