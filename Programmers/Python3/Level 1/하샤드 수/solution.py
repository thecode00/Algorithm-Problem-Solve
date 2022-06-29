# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True
    temp = list(str(x))
    temp = sum(list(map(int, temp)))
    return answer if x % temp == 0 else False
