# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for par in s:
        if par == "(":
            stack.append("(")
        else:
            if not stack:
                return False
            stack.pop()
    return False if stack else True