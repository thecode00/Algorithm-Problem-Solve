# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    length = len(s)
    # 길이가 홀수일땐 중간값만 짝수일땐 문자열을 슬라이스해서 반환
    return s[length // 2] if length % 2 != 0 else s[(length // 2) - 1: (length // 2) + 1]
