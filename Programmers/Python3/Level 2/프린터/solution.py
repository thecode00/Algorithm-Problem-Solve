# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque


def solution(priorities, location):
    answer = 0
    # enumerate로 자신의 중요도와 인덱스를 뽑음
    printer = deque([(pri, idx) for idx, pri in enumerate(priorities)])
    print(printer)
    while printer:
        cmd = printer.popleft()
        # 자신보다 높은 중요도를 가지고있는 프린트가 있다면 프린트를 미룸
        if printer and max(printer)[0] > cmd[0]:
            printer.append(cmd)
        else:
            answer += 1
            # 자신보다 중요도가 높은 프린트가 있는데 프린트가 안되므로 else문에서 체크를 함
            if cmd[1] == location:
                break
    return answer
