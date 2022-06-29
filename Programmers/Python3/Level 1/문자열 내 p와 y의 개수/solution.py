# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    # 바로 Boolean 반환
    return s.count("P") + s.count("p") == s.count("Y") + s.count("y")
