# https://school.programmers.co.kr/learn/courses/30/lessons/43163


from collections import deque


def solution(begin, target, words):
    if target not in words:  # words속에 타겟이 없으면 못만들거나 begin이 target이거나 둘중한개이므로 0을 반환
        return 0
    queue = deque()
    queue.append((begin, 0))
    length = len(begin)
    while queue:
        now, count = queue.popleft()
        if now == target:
            return count
        for word in words:
            diff = 0
            for idx in range(length):
                if now[idx] != word[idx]:
                    diff += 1
            if diff == 1:  # 다른 알파벳이 1개인 경우만 변환
                queue.append((word, count + 1))
    return 0
