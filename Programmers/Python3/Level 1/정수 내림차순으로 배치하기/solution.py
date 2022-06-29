# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = list(str(n))   # n을 문자열로 변환시켜 각 자리수마다 리스트 원소로 넣음
    answer.sort(reverse=True)
    return int("".join(answer))
