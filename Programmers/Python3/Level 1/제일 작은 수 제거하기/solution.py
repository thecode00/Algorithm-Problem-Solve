# https://programmers.co.kr/learn/courses/30/lessons/12935

from audioop import reverse


def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))    # arr에서 가장 작은값 제거
    return arr
