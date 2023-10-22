# https://www.acmicpc.net/problem/1213

from collections import Counter
import sys

input = sys.stdin.readline


def valid(count: Counter) -> bool:
    """펠린드롬으로 만들수있는 문자열인지 확인하는 함수

    Args:
        count: 문자열 카운터

    Returns:
        펠린드롬으로 만들수있는 문자일경우 True반환
    """
    odd = 0
    for num in count.values():
        odd += num % 2

    return odd <= 1  # 펠린드롬은 홀수가 여러개면 만들수없음


def solve() -> None:
    name = input().rstrip()
    count = Counter(name)
    if not valid(count):  # 펠린드롬으로 만들수없을때 출력
        print("I'm Sorry Hansoo")
        return

    result = [None] * len(name)
    left, right = 0, len(name) - 1
    # 사전순으로 꺼내서 left, right인덱스에 삽입
    for c in sorted(count.keys()):
        if count[c] % 2 == 1:   # 홀수가 있을경우 가운데에 삽입
            result[len(name) // 2] = c
        for _ in range(count[c] // 2):
            result[left], result[right] = c, c
            left += 1
            right -= 1
    print("".join(result))


solve()
