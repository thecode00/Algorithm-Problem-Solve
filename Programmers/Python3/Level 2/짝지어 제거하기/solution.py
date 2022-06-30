# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    for num in s:
        if stack:   # stack이 비어있지 않을때
            if stack[-1] == num:
                stack.pop()
            else:
                stack.append(num)
        else:
            stack.append(num)

    return 0 if stack else 1  # 마지막에 stack이 비어있지않으면 제거 실패이므로 1반환
