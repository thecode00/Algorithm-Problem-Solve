# https://school.programmers.co.kr/learn/courses/30/lessons/42888

from collections import deque


def solution(record):
    users = {}  # 유저 정보 딕셔너리
    for string in record:
        temp = string.split()
        if len(temp) == 3:  # Enter나 Leave때 유저정보를 저장
            users[temp[1]] = temp[2]
    answer = []
    for string in record:
        temp = string.split()
        if temp[0] == "Enter":
            answer.append("{0}님이 들어왔습니다.".format(users[temp[1]]))
        elif temp[0] == "Leave":
            answer.append("{0}님이 나갔습니다.".format(users[temp[1]]))
    return answer


def solution(record):
    print_queue = deque()
    users = {}
    # 나중에 출력해야될 순서를 덱에 담고 유저의 최종닉네임을 저장
    for s in record:
        cmd = s.split()
        if cmd[0] == "Enter":
            users[cmd[1]] = cmd[2]
            print_queue.append(["e", cmd[1]])
        elif cmd[0] == "Leave":
            print_queue.append(["l", cmd[1]])
        else:
            users[cmd[1]] = cmd[2]

    result = []
    while print_queue:
        cmd, id = print_queue.popleft()
        if cmd == "e":
            result.append(f"{users[id]}님이 들어왔습니다.")
        else:
            result.append(f"{users[id]}님이 나갔습니다.")
    return result
