# https://school.programmers.co.kr/learn/courses/30/lessons/43164


from collections import defaultdict, deque


def solution(tickets):
    airport = defaultdict(list)
    for start, end in tickets:
        airport[start].append(end)

    for key in airport:
        airport[key] = sorted(airport[key], reverse=True)
    print(airport)

    answer = []
    stack = ["ICN"]
    while stack:
        cur = stack.pop()
        if not airport[cur]:
            answer.append(cur)
        else:
            stack.append(cur)
            stack.append(airport[cur].pop())

    return answer
