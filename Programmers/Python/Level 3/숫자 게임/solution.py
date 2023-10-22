# https://school.programmers.co.kr/learn/courses/30/lessons/12987

from bisect import bisect_right


def solution(A, B):  # 첫번째 코드
    A.sort()
    B.sort()
    used = [False] * len(B)
    win = 0
    # A의 카드보다 큰 수 중에서 가장 차이가 적은 카드를 B에서 이진탐색을 통해 탐색
    for card in A:
        index = bisect_right(B, card)
        while index < len(B):
            if not used[index]:
                win += 1
                used[index] = True
                break
            index += 1
    return win


def solution(A, B):  # 두번째 코드
    A.sort()
    B.sort()
    win = 0
    a_index = 0
    # A와 B의 작은값부터 비교를 해가는 방식
    for card in B:
        if card > A[a_index]:
            a_index += 1
            win += 1
    return win
