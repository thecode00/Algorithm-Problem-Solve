# https://programmers.co.kr/learn/courses/30/lessons/12918


def solution(s):
    # isdigit함수는 문자열이 모두 숫자면 True를 반환
    return True if (len(s) == 4 or len(s) == 6) and s.isdigit() else False
