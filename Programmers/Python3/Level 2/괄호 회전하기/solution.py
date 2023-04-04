# https://school.programmers.co.kr/learn/courses/30/lessons/76502


from collections import deque


def solution(s):
    parenthesis = {")": "(", "}": "{", "]": "["}
    dp = [False for _ in range(len(s))]  # n번 회전시 올바른 문자열인지 저장하는 리스트
    queue = deque(s)
    count = 0

    for idx in range(len(s)):
        if idx != 0 and dp[idx - 1]:    # 만약 회전하기 전 문자열이 올바른 문자열이었다면 회전후에는 괄호가 망가지므로 넘어감
            queue.append(queue.popleft())
            continue
        flag = True  # 올바른 괄호 문자열인지 확인하는 플래그
        stack = []
        for p in queue:
            if p in parenthesis:
                if not stack or stack[-1] != parenthesis[p]:
                    flag = False
                    break
                stack.pop()
            else:
                stack.append(p)
        else:   # 탐색이 끝난후에도 stack에 괄호가남아있다면 열린괄호가 있다는 뜻
            if stack:
                flag = False

        queue.append(queue.popleft())   # 문자열 회전
        if flag:
            dp[idx] = True
            count += 1

    return count
