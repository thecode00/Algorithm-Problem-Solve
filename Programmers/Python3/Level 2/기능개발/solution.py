# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)  # deque의 popleft가 리스트의 pop(0)보다 빠르므로 사용
    speeds = deque(speeds)
    answer = []
    count = 0
    time = 0
    while progresses:
        if progresses[0] + time * speeds[0] >= 100:    # 작업완료
            count += 1
            progresses.popleft()
            speeds.popleft()
        else:
            time += 1
            if count > 0:
                answer.append(count)
                count = 0
    answer.append(count)    # 마지막 작업 처리
    return answer


solution([93, 30, 55], [1, 30, 5])
