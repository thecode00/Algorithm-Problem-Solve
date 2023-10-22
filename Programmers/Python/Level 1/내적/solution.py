# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = 0
    for pair in zip(a, b):  # pair[0], pair[1]로도 쓸수 있지만 변수를 2개 선언하여 쓸수도 있음
        answer += (pair[0] * pair[1])
    return answer
