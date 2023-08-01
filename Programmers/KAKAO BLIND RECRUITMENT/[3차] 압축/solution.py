# https://school.programmers.co.kr/learn/courses/30/lessons/17684

import string


def solution(msg):
    # 모든 단일 알파벳을 저장
    index_num = {s: idx + 1 for idx, s in enumerate(string.ascii_uppercase)}
    left = 0
    insert_num = 27
    answer = []
    while left < len(msg):
        right = left
        # msg[left: right] = msg의 left가 시작인 index_num에 저장되어있는 가장 긴 문자열
        while right < len(msg) and msg[left: right + 1] in index_num:
            right += 1
        answer.append(index_num[msg[left: right]])
        index_num[msg[left: right + 1]] = insert_num    # 새로운 문자열을 넣음
        insert_num += 1
        left = right
    return answer


print(solution("KAKAO"))
