# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    num = n ** .5
    if num == int(num):   # 정수 제곱근일때
        return (num + 1) ** 2
    return -1
