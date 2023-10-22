# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    if a == b:
        return a
    if a > b:   # 계산하기 쉽게 a가 b보다 클땐 값을 바꿔줌
        a, b = b, a
    answer = 0
    for num in range(a, b + 1):
        answer += num
    return answer
