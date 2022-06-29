# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    s = sorted(list(s), reverse=True)
    return "".join(s)
