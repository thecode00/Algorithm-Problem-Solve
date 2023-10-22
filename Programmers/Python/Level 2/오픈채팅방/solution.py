# https://programmers.co.kr/learn/courses/30/lessons/42888

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
