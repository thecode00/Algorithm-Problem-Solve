# https://school.programmers.co.kr/learn/courses/30/lessons/159994

from collections import deque


def solution(cards1, cards2, goal):
    cards1, cards2 = deque(cards1), deque(cards2)
    for word in goal:
        if cards1 and cards1[0] == word:
            cards1.popleft()
        elif cards2 and cards2[0] == word:
            cards2.popleft()
        else:
            return "No"

    return "Yes"
